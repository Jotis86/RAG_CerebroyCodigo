<div align="center">

![Brain and Code Banner](./assets/banner.png)

# 🧠 RAG System - Brain and Code

### RAG System for the educational repository [Brain and Code](https://github.com/Jotis86/CerebroyCodigo)

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io/)
[![Cohere](https://img.shields.io/badge/Cohere-5.5+-green.svg)](https://cohere.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)](https://www.docker.com/)

---

### 📊 Project Statistics

![Lines of Code](https://img.shields.io/badge/Lines%20of%20Code-1500+-blueviolet)
![Components](https://img.shields.io/badge/Components-7-success)
![Dependencies](https://img.shields.io/badge/Dependencies-10+-orange)
![Chunks Indexed](https://img.shields.io/badge/Chunks%20Indexed-38-informational)
![Response Time](https://img.shields.io/badge/Response%20Time-2--3s-green)

</div>

---

## 📖 Table of Contents

- [Features](#-features)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [RAG Architecture](#-rag-architecture)
- [Docker Usage](#-docker-usage)
- [Configuration](#-configuration)
- [Usage Examples](#-usage-examples)
- [Technologies](#-technologies)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## ✨ Features

- 🤖 **Complete RAG System** - Contextual information retrieval with augmented generation
- 🔍 **Semantic Search** - Finds information by meaning, not exact words
- 🌍 **Multilingual Embeddings** - Spanish text processing using Cohere
- 📊 **Vector Database** - ChromaDB for efficient storage and search
- 💬 **Conversational Interface** - Intuitive chat with persistent history
- 📚 **Full Transparency** - Visualization of sources used in each response
- 💡 **Suggested Questions** - Guides users with query examples
- 🐳 **Dockerized** - Easy container deployment
- ⚙️ **Highly Configurable** - Adjust models, parameters, and behavior

---

## 🚀 Quick Start

### Option A: Local Installation (Development)

#### 1️⃣ Clone and prepare environment

```bash
git clone <your-repo>
cd RAG_CerebroyCodigo

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### 2️⃣ Configure Cohere API Key

1. Get your **FREE** API key at [Cohere Dashboard](https://dashboard.cohere.com/api-keys)
2. Create configuration file:

```bash
cp .env.example .env
```

3. Edit `.env` and add your API key:

```bash
COHERE_API_KEY=your-api-key-here
```

#### 3️⃣ Run the application

```bash
# Option 1: Direct command
python -m streamlit run src/app.py

# Option 2: Startup script
./run.sh        # Linux/Mac
run.bat         # Windows
```

**Ready!** Open your browser at → http://localhost:8501

---

### Option B: With Docker 🐳 (Production)

#### Method 1: Docker Compose (Recommended)

```bash
# 1. Configure your API Key
echo "COHERE_API_KEY=your-api-key-here" > .env

# 2. Build and run
docker-compose up --build -d

# 3. Access the application
# http://localhost:8501
```

#### Method 2: Automatic Script

```bash
./docker-run.sh
```

#### Useful Docker Commands

```bash
# View logs in real-time
docker-compose logs -f

# Stop the application
docker-compose down

# Restart
docker-compose restart

# Check status
docker-compose ps
```

---

## 📁 Project Structure

```
RAG_CerebroyCodigo/
│
├── src/                        # 💻 Source code
│   ├── app.py                 # Main Streamlit application
│   │
│   ├── components/            # UI components
│   │   ├── chat_interface.py # Chat interface
│   │   └── sidebar.py        # Sidebar
│   │
│   ├── services/              # Business logic
│   │   ├── rag_service.py    # ⭐ Complete RAG system
│   │   └── cohere_client.py  # Cohere API client
│   │
│   └── utils/                 # Utilities
│       ├── config.py          # Centralized configuration
│       └── helpers.py         # Helper functions
│
├── data/                       # 📊 Source data
│   └── README.md              # Brain and Code repository content
│
├── assets/                     # 🎨 Assets
│   └── banner.png             # Project banner
│
├── tests/                      # 🧪 Unit tests
│   └── test_cohere_client.py
│
├── .env.example               # Configuration template
├── .gitignore                 # Files ignored by Git
├── .dockerignore              # Files ignored by Docker
│
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Docker image
├── docker-compose.yml         # Docker orchestration
│
├── run.sh                     # Unix startup script
├── run.bat                    # Windows startup script
├── docker-run.sh              # Docker script
│
├── INSTALAR.sh                # Auto-installer
└── README.md                  # This file
```

---

## 🏗️ RAG Architecture

### Operation Flow

```
┌─────────────────────────────────────────────────────────────┐
│ 1. USER ASKS A QUESTION                                      │
│    "What resources are available to learn Python?"           │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 2. EMBEDDING GENERATION                                      │
│    Cohere converts question to vector [0.23, -0.45...]      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 3. SEARCH IN CHROMADB                                        │
│    Finds the 4 most semantically similar chunks              │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 4. CONTEXT RETRIEVAL                                         │
│    - Chunk 1: "Python is a language..."                      │
│    - Chunk 2: "Resources for Python..."                      │
│    - Chunk 3: "Roadmap to Python..."                         │
│    - Chunk 4: "Exercism, Real Python..."                     │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 5. PROMPT CONSTRUCTION                                       │
│    System prompt + Context + User question                   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 6. GENERATION WITH COHERE LLM                                │
│    Model: command-r7b-12-2024                                │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│ 7. RESPONSE TO USER                                          │
│    Generated answer + Sources used                           │
└─────────────────────────────────────────────────────────────┘
```

### Technical Components

| Component | Technology | Function |
|-----------|------------|----------|
| **Interface** | Streamlit | Conversational UI |
| **LLM** | Cohere (command-r7b-12-2024) | Response generation |
| **Embeddings** | Cohere (embed-multilingual-v3.0) | Text vectorization |
| **Vector DB** | ChromaDB | Storage and search |
| **Orchestration** | LangChain | RAG pipeline |

### Document Processing

1. **Loading**: Reads `data/README.md` automatically
2. **Chunking**: Splits into 1000-token fragments with 200 overlap
3. **Embedding**: Generates vectors for each chunk
4. **Indexing**: Stores in ChromaDB
5. **Ready**: System prepared for queries

---

## 🐳 Docker Usage

### Container Features

- ✅ **Lightweight image** - Python 3.12 slim
- ✅ **Healthcheck** - Automatic health monitoring
- ✅ **Auto-restart** - Automatic restart on failure
- ✅ **Persistence** - Volume for ChromaDB
- ✅ **Hot-reload** - Updatable data without rebuild
- ✅ **Secure** - API keys as environment variables

### Build and Run

```bash
# With Docker Compose
docker-compose up --build -d

# Manual Docker
docker build -t rag-cerebro-codigo .
docker run -d -p 8501:8501 \
  -e COHERE_API_KEY=your-key \
  rag-cerebro-codigo
```

### Docker Management

```bash
# View logs
docker-compose logs -f

# Stop
docker-compose down

# Restart
docker-compose restart

# Full cleanup
docker-compose down -v
docker system prune -a
```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root:

```bash
# Cohere API Key (required)
COHERE_API_KEY=your-api-key-here
```


### Available Cohere Models

| Model | Parameters | Speed | Use Case |
|-------|------------|-------|----------|
| `command-r7b-12-2024` | 7B | ⚡⚡⚡ Very fast | Recommended for RAG |
| `command-r` | ~35B | ⚡⚡ Fast | Balanced |
| `command` | Large | ⚡ Normal | Complex tasks |

---

## 💡 Usage Examples

### Questions about Resources

```
✅ "What resources are available to learn Python?"
✅ "Where can I find Machine Learning tutorials?"
✅ "Give me resources about databases"
✅ "What tools do you recommend for data analysis?"
✅ "Where can I practice SQL online?"
✅ "What platforms do you recommend for learning AI?"
```

---

## 🛠️ Technologies

### Main Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.12+ | Base language |
| **Streamlit** | 1.28+ | Web framework |
| **Cohere** | 5.5+ | LLM and embeddings |
| **LangChain** | 0.1+ | RAG orchestration |
| **ChromaDB** | 0.4+ | Vector database |
| **Docker** | 20+ | Containerization |


### Useful Links

- 📦 [Brain and Code Repository](https://github.com/Jotis86/CerebroyCodigo)
- 🤖 [Cohere Documentation](https://docs.cohere.ai/)
- 🎨 [Streamlit Documentation](https://docs.streamlit.io/)
- 🔗 [LangChain Documentation](https://python.langchain.com/)
- 📊 [ChromaDB Documentation](https://docs.trychroma.com/)

---

## 🐛 Troubleshooting

### Error: "COHERE_API_KEY not configured"

**Cause:** The `.env` file doesn't exist or is misconfigured.

**Solution:**
```bash
# Check if it exists
ls -la .env

# If it doesn't exist, create it
cp .env.example .env

# Edit and add your API key
nano .env  # or use your preferred editor

# .env content:
COHERE_API_KEY=your-real-api-key-here
```

Get your API key at: https://dashboard.cohere.com/api-keys

---

### Error: "README.md not found"

**Cause:** The data file is not in the expected path.

**Solution:**
```bash
# Verify it exists
ls -la data/README.md

# If it's elsewhere, adjust the path in config.py
```

---

### Error installing dependencies

**Cause:** Issues with pip or system dependencies.

**Solution:**
```bash
# Update pip
pip install --upgrade pip

# Install again
pip install -r requirements.txt

# If ChromaDB fails (requires compilation)
# On macOS:
xcode-select --install

# On Ubuntu/Debian:
sudo apt-get install build-essential

# Then reinstall
pip install chromadb --no-cache-dir
```

---

### Changes not reflected in the app

**Cause:** Streamlit or Python cache.

**Solution:**
```bash
# Stop the app (Ctrl+C)

# Clear Streamlit cache
streamlit cache clear

# Optional: Clear compiled files
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null

# Restart the app
python -m streamlit run src/app.py

# In browser: Ctrl+Shift+R (force reload)
```

---

### Docker issues

**Solution:**
```bash
# View detailed logs
docker-compose logs -f

# Rebuild from scratch
docker-compose down -v
docker-compose up --build

# Clean all Docker
docker system prune -a
```

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. **Fork** the project
2. **Create a branch** for your feature:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit** your changes:
   ```bash
   git commit -m 'Add: feature description'
   ```
4. **Push** to the branch:
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Contribution Guidelines

- Follow the existing code style
- Add tests for new features
- Update documentation if necessary
- Ensure all tests pass

---

## 📄 License

This project is under the MIT License. See the `LICENSE` file for more details.

---

## 📞 Contact and Support

### Author

**Juan Durán**
- 📧 **Email:** jotaduranbon@gmail.com
- 📸 **Instagram:** [@cerebroycodigo](https://instagram.com/cerebroycodigo)
- 🐙 **GitHub:** [@Jotis86](https://github.com/Jotis86)

### Original Project

This is a RAG system developed for the educational repository:
- 📦 [Brain and Code](https://github.com/Jotis86/CerebroyCodigo)

---

## 🎯 How RAG Works

### Step 1: Indexing (Once at startup)
```
README.md (38 chunks)
       ↓
[Chunk 1] "Python is a language..."
[Chunk 2] "Machine Learning allows..."
[Chunk 3] "SQL is the language..."
       ↓
Cohere Embeddings
       ↓
[Vector 1] [0.23, -0.45, 0.67, ...]
[Vector 2] [0.12, 0.89, -0.34, ...]
[Vector 3] [-0.56, 0.23, 0.78, ...]
       ↓
ChromaDB (Vector database)
```

### Step 2: Query (Each question)
```
Your question: "How to learn Python?"
       ↓
Cohere Embeddings
       ↓
Question vector: [0.25, -0.43, 0.65, ...]
       ↓
ChromaDB: Similarity search
       ↓
Top 4 most similar chunks:
1. "Python is a language..." (similarity: 0.92)
2. "Resources for Python..." (similarity: 0.88)
3. "Roadmap to Python..." (similarity: 0.85)
4. "Exercism, Real Python..." (similarity: 0.82)
       ↓
Cohere LLM receives:
- Your question
- The 4 context chunks
       ↓
Generates coherent and contextualized response
       ↓
Shows response + sources
```

---

**💡 Developed with ❤️ by Jotis**

*Professional RAG system for knowledge exploration with AI*

---

<div align="center">

**If you found this useful, don't forget to give it a ⭐**

[⬆ Back to top](#-rag-system---brain-and-code)

</div>
