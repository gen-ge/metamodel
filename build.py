#!/usr/bin/env python3
"""
🏗️ Context Navigator - Build Script Simplificado
Sistema de build leve focado apenas no essencial

COMPORTAMENTO:
- Cria pacote .tar.gz para distribuição
- Copia arquivos necessários
- Cria estrutura de instalação
- NÃO duplica funcionalidade do Makefile

USO:
    python3 build.py                    # Build padrão
    python3 build.py --version 2.0.0    # Build com versão
    python3 build.py --clean            # Apenas limpar
"""

import os
import sys
import shutil
import tarfile
from pathlib import Path
from datetime import datetime
import argparse

def clean_directories():
    """Limpa diretórios de build"""
    build_dir = Path("build")
    dist_dir = Path("dist")
    
    for directory in [build_dir, dist_dir]:
        if directory.exists():
            shutil.rmtree(directory)
            print(f"🧹 Removido: {directory}")

def create_package(version: str | None = None):
    """Cria pacote para distribuição"""
    if not version:
        version = f"dev-{datetime.now().strftime('%Y%m%d-%H%M')}"
    
    # Diretórios
    src_dir = Path("src/context_navigator")
    build_dir = Path("build")
    dist_dir = Path("dist")
    package_dir = build_dir / f"context-navigator-{version}"
    
    # Criar estrutura
    for directory in [build_dir, dist_dir, package_dir]:
        directory.mkdir(exist_ok=True)
    
    print(f"📦 Criando pacote versão: {version}")
    
    # Copiar instalador unificado
    install_source = src_dir / "installer" / "install.py"
    install_dest = package_dir / "install.py"
    if install_source.exists():
        shutil.copy2(install_source, install_dest)
        print("✅ Copiado: install.py (unificado)")
    else:
        print("❌ install.py não encontrado")
        return False
    
    # Copiar source/
    source_dest = package_dir / "source"
    source_dest.mkdir(exist_ok=True)
    
    # Arquivos essenciais para copiar
    files_to_copy = [
        "core/",
        "scripts/",
        "templates/", 
        "installer/",
        "context.rule",
        "__init__.py"
    ]
    
    for item in files_to_copy:
        source_path = src_dir / item
        dest_path = source_dest / item
        
        if not source_path.exists():
            print(f"⚠️ Arquivo não encontrado: {item}")
            continue
            
        if source_path.is_dir():
            shutil.copytree(source_path, dest_path)
        else:
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, dest_path)
        print(f"✅ Copiado: {item}")
    
    # Copiar docs e arquivos do projeto
    project_files = ["docs/", "examples/", "README.md", "LICENSE"]
    for item in project_files:
        source_path = Path(item)
        dest_path = package_dir / item
        
        if not source_path.exists():
            continue
            
        if source_path.is_dir():
            shutil.copytree(source_path, dest_path)
        else:
            shutil.copy2(source_path, dest_path)
        print(f"✅ Copiado: {item}")
    
    # Criar .tar.gz
    tarball_path = dist_dir / f"context-navigator-{version}.tar.gz"
    
    with tarfile.open(tarball_path, 'w:gz') as tar:
        tar.add(package_dir, arcname=f"context-navigator-{version}")
    
    # Criar alias "latest"
    latest_path = dist_dir / "context-navigator-latest.tar.gz"
    shutil.copy2(tarball_path, latest_path)
    
    size_kb = tarball_path.stat().st_size / 1024
    print(f"🎉 Pacote criado: {tarball_path} ({size_kb:.1f} KB)")
    print(f"🔗 Alias criado: {latest_path}")
    
    return True

def main():
    parser = argparse.ArgumentParser(description='Context Navigator Build Script Simplificado')
    parser.add_argument('--version', '-v', help='Versão do build')
    parser.add_argument('--clean', action='store_true', help='Apenas limpar diretórios')
    
    args = parser.parse_args()
    
    if args.clean:
        clean_directories()
        print("✅ Limpeza concluída")
        return 0
    
    print("🏗️ Context Navigator - Build Simplificado")
    
    # Limpar primeiro
    clean_directories()
    
    # Criar pacote
    if create_package(args.version):
        print("✅ Build concluído com sucesso!")
        print("💡 Para testar: cd dist && tar -xzf context-navigator-*.tar.gz")
        return 0
    else:
        print("❌ Falha no build")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 