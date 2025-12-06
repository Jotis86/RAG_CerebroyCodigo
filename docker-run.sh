#!/bin/bash

# Script para ejecutar el contenedor Docker del Sistema RAG

echo "🐳 Sistema RAG - Cerebro y Código"
echo "=================================="
echo ""

# Verificar si Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "❌ Docker no está instalado"
    echo "   Instálalo desde: https://docs.docker.com/get-docker/"
    exit 1
fi

# Verificar si existe el archivo .env
if [ ! -f ".env" ]; then
    echo "⚠️  No se encontró el archivo .env"
    echo ""
    echo "📝 Creando archivo .env..."
    echo "   Por favor, edita el archivo y añade tu COHERE_API_KEY"
    echo ""
    echo "COHERE_API_KEY=tu-api-key-aqui" > .env
    echo "✅ Archivo .env creado"
    echo ""
    echo "⚠️  IMPORTANTE: Edita .env y añade tu API key de Cohere"
    echo "   Luego vuelve a ejecutar este script"
    exit 1
fi

# Verificar que COHERE_API_KEY esté configurada
source .env
if [ -z "$COHERE_API_KEY" ] || [ "$COHERE_API_KEY" == "tu-api-key-aqui" ]; then
    echo "❌ COHERE_API_KEY no está configurada correctamente"
    echo "   Edita el archivo .env y añade tu API key"
    exit 1
fi

echo "✅ Configuración verificada"
echo ""

# Preguntar si usar docker-compose o docker run
echo "¿Cómo quieres ejecutar el contenedor?"
echo "1) docker-compose (recomendado)"
echo "2) docker run (manual)"
echo ""
read -p "Opción [1/2]: " opcion

case $opcion in
    1)
        echo ""
        echo "🔨 Construyendo y ejecutando con docker-compose..."
        docker-compose up --build -d
        echo ""
        echo "✅ Contenedor iniciado!"
        echo ""
        echo "📍 Accede a la aplicación en: http://localhost:8501"
        echo ""
        echo "💡 Comandos útiles:"
        echo "   - Ver logs: docker-compose logs -f"
        echo "   - Detener: docker-compose down"
        echo "   - Reiniciar: docker-compose restart"
        ;;
    2)
        echo ""
        echo "🔨 Construyendo imagen..."
        docker build -t rag-cerebro-codigo .
        echo ""
        echo "🚀 Ejecutando contenedor..."
        docker run -d \
            --name rag-cerebro-codigo \
            -p 8501:8501 \
            -e COHERE_API_KEY=$COHERE_API_KEY \
            -v $(pwd)/data:/app/data:ro \
            rag-cerebro-codigo
        echo ""
        echo "✅ Contenedor iniciado!"
        echo ""
        echo "📍 Accede a la aplicación en: http://localhost:8501"
        echo ""
        echo "💡 Comandos útiles:"
        echo "   - Ver logs: docker logs -f rag-cerebro-codigo"
        echo "   - Detener: docker stop rag-cerebro-codigo"
        echo "   - Eliminar: docker rm rag-cerebro-codigo"
        ;;
    *)
        echo "Opción no válida"
        exit 1
        ;;
esac

echo ""
echo "🎉 ¡Disfruta del Sistema RAG!"

