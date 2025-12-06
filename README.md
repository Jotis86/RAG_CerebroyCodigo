<div align="center">

![Banner Cerebro y Código](./assets/banner.png)

# 🧠 Sistema RAG - Cerebro y Código

### Sistema de RAG para el repositorio educativo [Cerebro y Código](https://github.com/Jotis86/CerebroyCodigo)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Cohere](https://img.shields.io/badge/Cohere-5.5+-green.svg)](https://cohere.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

---

### 📊 Estadísticas del Proyecto

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-1500+-blueviolet)
![Components](https://img.shields.io/badge/Components-7-success)
![Dependencies](https://img.shields.io/badge/Dependencies-10+-orange)
![Chunks Indexed](https://img.shields.io/badge/Chunks%20Indexed-38-informational)
![Response Time](https://img.shields.io/badge/Response%20Time-2--3s-green)

</div>

---

## 📖 Tabla de Contenidos

- [Características](#-características)
- [Inicio Rápido](#-inicio-rápido)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Arquitectura RAG](#-arquitectura-rag)
- [Uso con Docker](#-uso-con-docker)
- [Configuración](#-configuración)
- [Ejemplos de Uso](#-ejemplos-de-uso)
- [Tecnologías](#-tecnologías)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribuciones](#-contribuciones)
- [Licencia](#-licencia)

---

## ✨ Características

- 🤖 **Sistema RAG Completo** - Recuperación de información contextual con generación aumentada
- 🔍 **Búsqueda Semántica** - Encuentra información por significado, no por palabras exactas
- 🌍 **Embeddings Multilingües** - Procesamiento de texto en español usando Cohere
- 📊 **Base de Datos Vectorial** - ChromaDB para almacenamiento y búsqueda eficiente
- 💬 **Interfaz Conversacional** - Chat intuitivo con historial persistente
- 📚 **Transparencia Total** - Visualización de fuentes utilizadas en cada respuesta
- 💡 **Preguntas Sugeridas** - Guía al usuario con ejemplos de consultas
- 🐳 **Dockerizado** - Fácil despliegue en contenedores
- ⚙️ **Altamente Configurable** - Ajusta modelos, parámetros y comportamiento

---

## 🚀 Inicio Rápido

### Opción A: Instalación Local (Desarrollo)

#### 1️⃣ Clonar y preparar entorno

```bash
git clone <tu-repo>
cd RAG_CerebroyCodigo

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

#### 2️⃣ Configurar API Key de Cohere

1. Obtén tu API key **gratuita** en [Cohere Dashboard](https://dashboard.cohere.com/api-keys)
2. Crea el archivo de configuración:

```bash
cp .env.example .env
```

3. Edita `.env` y añade tu API key:

```bash
COHERE_API_KEY=tu-api-key-aqui
```

#### 3️⃣ Ejecutar la aplicación

```bash
# Opción 1: Comando directo
python -m streamlit run src/app.py

# Opción 2: Script de inicio
./run.sh        # Linux/Mac
run.bat         # Windows
```

**¡Listo!** Abre tu navegador en → http://localhost:8501

---

### Opción B: Con Docker 🐳 (Producción)

#### Método 1: Docker Compose (Recomendado)

```bash
# 1. Configura tu API Key
echo "COHERE_API_KEY=tu-api-key-aqui" > .env

# 2. Construye y ejecuta
docker-compose up --build -d

# 3. Accede a la aplicación
# http://localhost:8501
```

#### Método 2: Script Automático

```bash
./docker-run.sh
```

#### Comandos Útiles de Docker

```bash
# Ver logs en tiempo real
docker-compose logs -f

# Detener la aplicación
docker-compose down

# Reiniciar
docker-compose restart

# Ver estado
docker-compose ps
```

---

## 📁 Estructura del Proyecto

```
RAG_CerebroyCodigo/
│
├── src/                        # 💻 Código fuente
│   ├── app.py                 # Aplicación principal Streamlit
│   │
│   ├── components/            # Componentes de UI
│   │   ├── chat_interface.py # Interfaz de chat
│   │   └── sidebar.py        # Barra lateral
│   │
│   ├── services/              # Lógica de negocio
│   │   ├── rag_service.py    # ⭐ Sistema RAG completo
│   │   └── cohere_client.py  # Cliente API Cohere
│   │
│   └── utils/                 # Utilidades
│       ├── config.py          # Configuración centralizada
│       └── helpers.py         # Funciones auxiliares
│
├── data/                       # 📊 Datos fuente
│   └── README.md              # Contenido del repositorio Cerebro y Código
│
├── tests/                      # 🧪 Tests unitarios
│   └── test_cohere_client.py
│
├── .env.example               # Plantilla de configuración
├── .gitignore                 # Archivos ignorados por Git
├── .dockerignore              # Archivos ignorados por Docker
│
├── requirements.txt           # Dependencias Python
├── Dockerfile                 # Imagen Docker
├── docker-compose.yml         # Orquestación Docker
│
├── run.sh                     # Script inicio Unix
├── run.bat                    # Script inicio Windows
├── docker-run.sh              # Script Docker
│
├── INSTALAR.sh                # Instalador automático
└── README.md                  # Este archivo
```

---

## 🏗️ Arquitectura RAG

### Flujo de Funcionamiento

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USUARIO HACE UNA PREGUNTA                                 │
│    "¿Qué recursos hay para aprender Python?"                 │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. GENERACIÓN DE EMBEDDING                                   │
│    Cohere convierte la pregunta en vector [0.23, -0.45...]  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. BÚSQUEDA EN CHROMADB                                      │
│    Encuentra los 4 chunks más similares semánticamente       │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. RECUPERACIÓN DE CONTEXTO                                  │
│    - Chunk 1: "Python es un lenguaje..."                     │
│    - Chunk 2: "Recursos para Python..."                      │
│    - Chunk 3: "Roadmap to Python..."                         │
│    - Chunk 4: "Exercism, Real Python..."                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. CONSTRUCCIÓN DEL PROMPT                                   │
│    System prompt + Contexto + Pregunta del usuario           │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. GENERACIÓN CON COHERE LLM                                 │
│    Modelo: command-r7b-12-2024                               │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. RESPUESTA AL USUARIO                                      │
│    Respuesta generada + Fuentes utilizadas                   │
└─────────────────────────────────────────────────────────────┘
```

### Componentes Técnicos

| Componente | Tecnología | Función |
|------------|------------|---------|
| **Interfaz** | Streamlit | UI conversacional |
| **LLM** | Cohere (command-r7b-12-2024) | Generación de respuestas |
| **Embeddings** | Cohere (embed-multilingual-v3.0) | Vectorización de texto |
| **Vector DB** | ChromaDB | Almacenamiento y búsqueda |
| **Orquestación** | LangChain | Pipeline RAG |

### Procesamiento de Documentos

1. **Carga**: Lee `data/README.md` automáticamente
2. **Chunking**: Divide en fragmentos de 1000 tokens con 200 de overlap
3. **Embedding**: Genera vectores para cada chunk
4. **Indexación**: Almacena en ChromaDB
5. **Listo**: El sistema está preparado para consultas

---

## 🐳 Uso con Docker

### Características del Contenedor

- ✅ **Imagen ligera** - Python 3.12 slim
- ✅ **Healthcheck** - Monitoreo automático de salud
- ✅ **Auto-restart** - Reinicio automático ante fallos
- ✅ **Persistencia** - Volumen para ChromaDB
- ✅ **Hot-reload** - Datos actualizables sin reconstruir
- ✅ **Seguro** - API keys como variables de entorno


---

## ⚙️ Configuración


### Variables de Entorno

Crea un archivo `.env` en la raíz:

```bash
# API Key de Cohere (obligatoria)
COHERE_API_KEY=tu-api-key-aqui
```

### Modelos Disponibles de Cohere

| Modelo | Parámetros | Velocidad | Uso |
|--------|------------|-----------|-----|
| `command-r7b-12-2024` | 7B | ⚡⚡⚡ Muy rápido | Recomendado para RAG |
| `command-r` | ~35B | ⚡⚡ Rápido | Balanceado |
| `command` | Grande | ⚡ Normal | Tareas complejas |

---

## 💡 Ejemplos de Uso

### Preguntas sobre Recursos

```
✅ "¿Qué recursos hay para aprender Python?"
✅ "¿Dónde puedo encontrar tutoriales de Machine Learning?"
✅ "Dame recursos sobre bases de datos"
✅ "¿Qué herramientas recomiendas para análisis de datos?"
✅ "¿Dónde puedo practicar SQL en línea?"
✅ "¿Qué plataformas recomiendas para aprender IA?"
✅ "Dame enlaces para desplegar aplicaciones"
```

---

## 🛠️ Tecnologías

### Stack Principal

| Tecnología | Versión | Uso |
|------------|---------|-----|
| **Python** | 3.12+ | Lenguaje base |
| **Streamlit** | 1.28+ | Framework web |
| **Cohere** | 5.5+ | LLM y embeddings |
| **LangChain** | 0.1+ | Orquestación RAG |
| **ChromaDB** | 0.4+ | Base de datos vectorial |
| **Docker** | 20+ | Contenedorización |

### Dependencias Principales

```txt
streamlit>=1.28.0
cohere>=5.5.0
langchain>=0.1.0
langchain-community>=0.0.10
langchain-cohere>=0.1.0
chromadb>=0.4.18
tiktoken>=0.5.1
python-dotenv>=1.0.0
```

### Enlaces Útiles

- 📦 [Repositorio Cerebro y Código](https://github.com/Jotis86/CerebroyCodigo)
- 🤖 [Documentación Cohere](https://docs.cohere.ai/)
- 🎨 [Documentación Streamlit](https://docs.streamlit.io/)
- 🔗 [Documentación LangChain](https://python.langchain.com/)
- 📊 [Documentación ChromaDB](https://docs.trychroma.com/)

---

## 🐛 Solución de Problemas

### Error: "COHERE_API_KEY no está configurada"

**Causa:** No existe el archivo `.env` o está mal configurado.

**Solución:**
```bash
# Verifica que existe
ls -la .env

# Si no existe, créalo
cp .env.example .env

# Edita y añade tu API key
nano .env  # o usa tu editor favorito

# Contenido del .env:
COHERE_API_KEY=tu-api-key-real-aqui
```

Obtén tu API key en: https://dashboard.cohere.com/api-keys

---

### Error: "README.md no encontrado"

**Causa:** El archivo de datos no está en la ruta esperada.

**Solución:**
```bash
# Verifica que existe
ls -la data/README.md

# Si está en otro lugar, ajusta la ruta en config.py
```

---

### Error al instalar dependencias

**Causa:** Problemas con pip o dependencias del sistema.

**Solución:**
```bash
# Actualiza pip
pip install --upgrade pip

# Instala de nuevo
pip install -r requirements.txt

# Si falla ChromaDB (requiere compilación)
# En macOS:
xcode-select --install

# En Ubuntu/Debian:
sudo apt-get install build-essential

# Luego reinstala
pip install chromadb --no-cache-dir
```

---

### Problemas con Docker

**Solución:**
```bash
# Ver logs detallados
docker-compose logs -f

# Reconstruir desde cero
docker-compose down -v
docker-compose up --build

# Limpiar todo Docker
docker system prune -a
```

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas! Sigue estos pasos:

1. **Fork** el proyecto
2. **Crea una rama** para tu feature:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** tus cambios:
   ```bash
   git commit -m 'Add: descripción del cambio'
   ```
4. **Push** a la rama:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Abre un Pull Request**

### Guías de Contribución

- Sigue el estilo de código existente
- Añade tests para nuevas funcionalidades
- Actualiza la documentación si es necesario
- Asegúrate de que todos los tests pasen

---

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

```
MIT License

Copyright (c) 2025 Juan Durán

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 📞 Contacto y Soporte

### Autor

**Juan Durán**
- 📧 **Email:** jotaduranbon@gmail.com
- 📸 **Instagram:** [@cerebroycodigo](https://instagram.com/cerebroycodigo)
- 🐙 **GitHub:** [@Jotis86](https://github.com/Jotis86)

### Proyecto Original

Este es un sistema RAG desarrollado para el repositorio educativo:
- 📦 [Cerebro y Código](https://github.com/Jotis86/CerebroyCodigo)


---

**💡 Desarrollado con ❤️ por Jotis**

*Sistema RAG profesional para exploración de conocimiento con IA* 

---

<div align="center">

**Si te ha sido útil, no olvides darle una ⭐**

[⬆ Volver arriba](#-sistema-rag---cerebro-y-código)

</div>
