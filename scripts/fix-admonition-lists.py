#!/usr/bin/env python3
"""
Script para corrigir formatação de listas em admonitions no MkDocs Material.

Problema: Listas numeradas dentro de admonitions precisam de linha em branco
antes da lista para renderizar corretamente.

Este script identifica e corrige automaticamente esses problemas.
"""

import os
import re
import sys
from pathlib import Path

ADMONITION_START_RE = re.compile(r"^(?:\?\?\?|!!!)\s+")
INDENTED_CONTENT_RE = re.compile(r"^(?: {4}|\t)")
BLOCK_START_RE = re.compile(r"^ {4}(?:[-*+]\s+|\d+\.\s+|>\s*)")
CURRENT_BLOCK_RE = re.compile(r"^ {4}(?:[-*+]\s+|\d+\.\s+|>\s*|```|~~~)")


def is_admonition_content(line):
    return line.strip() == "" or INDENTED_CONTENT_RE.match(line) is not None


def needs_blank_line_before_block(current_line, next_line):
    if current_line.strip() == "":
        return False

    if not INDENTED_CONTENT_RE.match(current_line):
        return False

    if CURRENT_BLOCK_RE.match(current_line):
        return False

    return BLOCK_START_RE.match(next_line) is not None


def fix_lists_in_admonitions(content):
    """
    Corrige blocos Markdown dentro de admonitions.

    O MkDocs Material precisa de uma linha em branco entre um parágrafo e uma
    lista/citação dentro de ???/!!!. Sem isso, os itens ficam colados no texto.
    """

    lines = content.splitlines()
    fixed_lines = []
    in_admonition = False

    for index, line in enumerate(lines):
        if ADMONITION_START_RE.match(line):
            in_admonition = True
        elif in_admonition and not is_admonition_content(line):
            in_admonition = False

        fixed_lines.append(line)

        if not in_admonition or index + 1 >= len(lines):
            continue

        next_line = lines[index + 1]
        if needs_blank_line_before_block(line, next_line):
            fixed_lines.append("    ")

    trailing_newline = "\n" if content.endswith("\n") else ""
    return "\n".join(fixed_lines) + trailing_newline

def validate_file(file_path):
    """
    Valida se um arquivo markdown tem problemas de formatação em admonitions.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Procura por padrões problemáticos
        issues = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Verifica se está dentro de um admonition
            if re.match(r'^\?\?\?|!!!', line):
                # Verifica as próximas linhas
                j = i + 1
                while j < len(lines) and lines[j].startswith('    '):
                    current_line = lines[j]
                    next_line = lines[j + 1] if j + 1 < len(lines) else ''
                    
                    # Lista sem linha em branco antes
                    if (re.match(r'^\s*(\d+\.|[-*+])\s+', current_line) and 
                        j > i + 1 and 
                        not lines[j - 1].strip() == '' and
                        lines[j - 1].strip().endswith(':')):
                        
                        issues.append({
                            'line': j + 1,
                            'type': 'lista_sem_linha_branca',
                            'content': current_line.strip(),
                            'previous': lines[j - 1].strip()
                        })
                    
                    j += 1
        
        return issues
    
    except Exception as e:
        print(f"Erro ao validar arquivo {file_path}: {e}")
        return []

def process_file(file_path, dry_run=False):
    """
    Processa um único arquivo markdown.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Aplica as correções somente dentro de admonitions.
        fixed_content = fix_lists_in_admonitions(original_content)
        
        # Verifica se houve mudanças
        if original_content != fixed_content:
            if dry_run:
                print(f"🔍 Arquivo precisa de correções: {file_path}")
                return True
            else:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(fixed_content)
                print(f"✅ Arquivo corrigido: {file_path}")
                return True
        else:
            if dry_run:
                print(f"✅ Arquivo OK: {file_path}")
            return False
    
    except Exception as e:
        print(f"❌ Erro ao processar arquivo {file_path}: {e}")
        return False

def find_markdown_files(directory):
    """
    Encontra todos os arquivos markdown em um diretório.
    """
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def main():
    """
    Função principal do script.
    """
    # Diretório padrão é a pasta docs do projeto
    docs_dir = Path(__file__).parent.parent / 'docs'
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("Uso: python fix-admonition-lists.py [opções] [arquivo_ou_diretorio]")
            print("")
            print("Opções:")
            print("  --dry-run, -n    Apenas verifica arquivos, não modifica")
            print("  --validate, -v  Modo validação detalhada")
            print("  --help, -h      Mostra esta ajuda")
            print("")
            print("Se nenhum arquivo for especificado, processa toda a pasta docs/")
            return
        
        command = sys.argv[1]
        target_path = sys.argv[2] if len(sys.argv) > 2 else docs_dir
        
        if command in ['--dry-run', '-n']:
            dry_run = True
        elif command in ['--validate', '-v']:
            # Modo validação
            if os.path.isfile(target_path):
                issues = validate_file(target_path)
                if issues:
                    print(f"🔍 Problemas encontrados em {target_path}:")
                    for issue in issues:
                        print(f"  Linha {issue['line']}: {issue['type']}")
                        print(f"    Anterior: '{issue['previous']}'")
                        print(f"    Atual: '{issue['content']}'")
                        print()
                else:
                    print(f"✅ Nenhum problema encontrado em {target_path}")
            else:
                print("Modo validação requer um arquivo específico")
            return
        else:
            # Se não é comando, é um arquivo/diretório
            target_path = command
            dry_run = False
    else:
        target_path = docs_dir
        dry_run = False
    
    # Verifica se o caminho existe
    if not os.path.exists(target_path):
        print(f"❌ Caminho não encontrado: {target_path}")
        return
    
    # Processa arquivo ou diretório
    if os.path.isfile(target_path):
        if not target_path.endswith('.md'):
            print("❌ Arquivo deve ser .md")
            return
        
        mode_text = "verificando" if dry_run else "corrigindo"
        print(f"🔧 {mode_text.title()} arquivo: {target_path}")
        process_file(target_path, dry_run)
    
    elif os.path.isdir(target_path):
        mode_text = "verificando" if dry_run else "corrigindo"
        print(f"🔧 {mode_text.title()} arquivos em: {target_path}")
        print()
        
        markdown_files = find_markdown_files(target_path)
        files_changed = 0
        
        for file_path in sorted(markdown_files):
            if process_file(file_path, dry_run):
                files_changed += 1
        
        print()
        if dry_run:
            print(f"📊 Resumo: {files_changed} de {len(markdown_files)} arquivos precisam de correções")
            if files_changed > 0:
                print("💡 Execute novamente sem --dry-run para aplicar as correções")
        else:
            print(f"📊 Resumo: {files_changed} de {len(markdown_files)} arquivos foram corrigidos")
    
    else:
        print(f"❌ Tipo de arquivo não suportado: {target_path}")

if __name__ == '__main__':
    main()
