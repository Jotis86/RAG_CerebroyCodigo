@echo off
REM Script para iniciar la aplicación RAG de Cerebro y Código en Windows

echo 🧠 Cerebro y Código - Sistema RAG
echo ==================================
echo.

REM Verificar si existe el entorno virtual
if not exist "venv\" (
    echo ⚠️  No se encontró el entorno virtual.
    echo 📦 Creando entorno virtual...
    python -m venv venv
    echo ✅ Entorno virtual creado
)

REM Activar entorno virtual
echo 🔄 Activando entorno virtual...
call venv\Scripts\activate.bat

REM Verificar si existen las dependencias
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo 📦 Instalando dependencias...
    pip install -r requirements.txt
    echo ✅ Dependencias instaladas
)

REM Verificar archivo .env
if not exist ".env" (
    echo ⚠️  No se encontró el archivo .env
    echo 📝 Copia .env.example a .env y añade tu API key
    echo.
    echo Pasos:
    echo 1. copy .env.example .env
    echo 2. Edita .env y añade: COHERE_API_KEY=tu-api-key
    echo 3. Ejecuta este script de nuevo
    pause
    exit /b 1
)

REM Verificar README.md en data
if not exist "data\README.md" (
    echo ⚠️  No se encontró data\README.md
    echo Por favor, verifica que el archivo existe
    pause
    exit /b 1
)

REM Limpiar terminal
cls

REM Iniciar la aplicación
echo 🚀 Iniciando aplicación...
echo 📍 La aplicación se abrirá en: http://localhost:8501
echo.
echo 💡 Presiona Ctrl+C para detener
echo.

python -m streamlit run src/app.py

