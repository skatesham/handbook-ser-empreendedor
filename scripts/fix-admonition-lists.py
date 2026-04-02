#!/usr/bin/env python3
"""
Script para corrigir formatação de listas em admonitions no MkDocs Material.

Problema: Listas numeradas dentro de admonitions precisam de linha em branco
antes da lista para renderizar corretamente.

Este script identifica e corrige automaticamente esses problemas.
"""

import re
import os
import sys
from pathlib import Path

def fix_lists_in_admonitions(content):
    """
    Corrige formatação de listas em admonitions.
    
    Padrões corrigidos:
    1. Listas numeradas sem linha em branco antes
    2. Listas com marcadores sem linha em branco antes
    """
    
    # Padrão para encontrar admonitions com listas sem linha em branco
    # Captura: ???/!!! + espaços + "título" + conteúdo
    admonition_pattern = r'(\?\?\?|!!!)\s+(\w+)\s+"([^"]+)"\s*\n((?:    .*\n)*)'
    
    def fix_admonition(match):
        prefix = match.group(1)
        admon_type = match.group(2)
        title = match.group(3)
        content = match.group(4)
        
        # Divide o conteúdo em linhas
        lines = content.split('\n')
        fixed_lines = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Verifica se a linha atual é um texto seguido por lista na próxima
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                
                # Padrão para lista numerada ou com marcadores
                is_list_item = re.match(r'^\s*(\d+\.|[-*+])\s+', next_line)
                
                # Se a linha atual termina com dois pontos e a próxima é lista
                if (line.strip().endswith(':') or line.strip().endswith('**O que fazer:**')) and is_list_item:
                    fixed_lines.append(line)  # Mantém a linha atual
                    fixed_lines.append('')   # Adiciona linha em branco
                    i += 1
                    continue
                
                # Padrão específico para "**O que fazer:**"
                if '**O que fazer:**' in line and not line.strip().endswith('**O que fazer:**'):
                    # Se contém "O que fazer" mas não termina com isso, pode precisar de linha em branco
                    if is_list_item:
                        fixed_lines.append(line)
                        fixed_lines.append('')
                        i += 1
                        continue
            
            fixed_lines.append(line)
            i += 1
        
        # Reconstrói o conteúdo
        fixed_content = '\n'.join(fixed_lines)
        
        return f"{prefix} {admon_type} \"{title}\"\n{fixed_content}"
    
    # Aplica a correção
    fixed_content = re.sub(admonition_pattern, fix_admonition, content, flags=re.MULTILINE)
    
    return fixed_content

def fix_specific_patterns(content):
    """
    Corrige padrões específicos conhecidos que causam problemas.
    """
    
    # Padrão 1: "**O que fazer:**" seguido diretamente por lista
    pattern1 = r'(\*\*O que fazer:\*\*)\s*\n\s*(\d+\.)'
    content = re.sub(pattern1, r'\1\n\n    \2', content)
    
    # Padrão 2: Texto terminando em ":" seguido por lista
    pattern2 = r'([^:\n]+:\s*)\n(\s{4,}[-*+]|\s{4,}\d+\.)'
    content = re.sub(pattern2, r'\1\n\n\2', content)
    
    # Padrão 3: "Adapte:" seguido por lista
    pattern3 = r'(Adapte:\s*)\n(\s{4,}[-*+]|\s{4,}\d+\.)'
    content = re.sub(pattern3, r'\1\n\n\2', content)
    
    return content

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
        
        # Aplica as correções
        fixed_content = fix_lists_in_admonitions(original_content)
        fixed_content = fix_specific_patterns(fixed_content)
        
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
