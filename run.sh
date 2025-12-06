#!/bin/bash

# Script para iniciar la aplicación RAG de Cerebro y Código

echo "🧠 Cerebro y Código - Sistema RAG"
echo "=================================="
echo ""

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "⚠️  No se encontró el entorno virtual."
    echo "📦 Creando entorno virtual..."
    python3 -m venv venv
    echo "✅ Entorno virtual creado"
fi

# Activar entorno virtual
echo "🔄 Activando entorno virtual..."
source venv/bin/activate

# Verificar si existen las dependencias
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Instalando dependencias..."
    pip install -r requirements.txt
    echo "✅ Dependencias instaladas"
fi

# Verificar archivo .env
if [ ! -f ".env" ]; then
    echo "⚠️  No se encontró el archivo .env"
    echo "📝 Copia .env.example a .env y añade tu API key"
    echo ""
    echo "Pasos:"
    echo "1. cp .env.example .env"
    echo "2. Edita .env y añade: COHERE_API_KEY=tu-api-key"
    echo "3. Ejecuta este script de nuevo"
    exit 1
fi

# Verificar README.md en data
if [ ! -f "data/README.md" ]; then
    echo "⚠️  No se encontró data/README.md"
    echo "Por favor, verifica que el archivo existe"
    exit 1
fi

# Limpiar terminal
clear

# Iniciar la aplicación
echo "🚀 Iniciando aplicación..."
echo "📍 La aplicación se abrirá en: http://localhost:8501"
echo ""
echo "💡 Presiona Ctrl+C para detener"
echo ""

python -m streamlit run src/app.py

