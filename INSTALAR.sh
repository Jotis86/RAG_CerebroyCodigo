#!/bin/bash

echo "🔧 Script de Instalación - Sistema RAG"
echo "======================================"
echo ""

# Detener si hay algún error
set -e

echo "📦 Paso 1/5: Eliminando entorno virtual anterior..."
rm -rf venv
echo "✅ Limpiado"
echo ""

echo "📦 Paso 2/5: Creando nuevo entorno virtual..."
python3 -m venv venv
echo "✅ Entorno virtual creado"
echo ""

echo "📦 Paso 3/5: Activando entorno virtual..."
source venv/bin/activate
echo "✅ Entorno activado"
echo ""

echo "📦 Paso 4/5: Actualizando pip..."
pip install --upgrade pip --quiet
echo "✅ Pip actualizado"
echo ""

echo "📦 Paso 5/5: Instalando dependencias..."
echo "   (Esto puede tomar 1-2 minutos...)"
pip install -r requirements.txt
echo ""
echo "✅ Dependencias instaladas correctamente"
echo ""

echo "═══════════════════════════════════════════════"
echo "✨ ¡INSTALACIÓN COMPLETA!"
echo "═══════════════════════════════════════════════"
echo ""
echo "📋 Próximos pasos:"
echo ""
echo "1. Activa el entorno virtual:"
echo "   source venv/bin/activate"
echo ""
echo "2. Configura tu API key (si no lo has hecho):"
echo "   cp .env.example .env"
echo "   # Luego edita .env y añade tu COHERE_API_KEY"
echo ""
echo "3. Ejecuta la aplicación:"
echo "   streamlit run src/app.py"
echo ""
echo "═══════════════════════════════════════════════"

