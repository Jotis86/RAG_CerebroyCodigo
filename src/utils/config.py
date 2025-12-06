"""
Configuración de la aplicación RAG.
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Cargar variables de entorno desde la raíz del proyecto
BASE_DIR = Path(__file__).parent.parent.parent  # RAG_CerebroyCodigo/
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)


class Config:
    """Configuración centralizada de la aplicación."""
    
    # Rutas (usar la BASE_DIR ya definida arriba)
    DATA_DIR = BASE_DIR / "data"
    README_PATH = DATA_DIR / "README.md"
    
    # API Keys
    COHERE_API_KEY = os.getenv("COHERE_API_KEY", "")
    
    # Configuración de la aplicación
    APP_TITLE = "🧠 Cerebro y Código - Asistente RAG"
    APP_DESCRIPTION = """
    Asistente virtual inteligente para el repositorio Cerebro y Código.
    Pregunta sobre recursos, tecnologías y rutas de aprendizaje.
    """
    
    # Configuración del modelo
    LLM_MODEL = "command-r7b-12-2024"  # Modelo ligero y rápido de Cohere
    EMBEDDING_MODEL = "embed-multilingual-v3.0"
    TEMPERATURE = 0.3
    MAX_TOKENS = 800
    
    # Configuración RAG
    CHUNK_SIZE = 1000
    CHUNK_OVERLAP = 200
    TOP_K_RETRIEVAL = 4
    
    # Configuración de ChromaDB
    COLLECTION_NAME = "cerebro_y_codigo"
    
    @classmethod
    def validate(cls):
        """Valida que la configuración sea correcta."""
        errors = []
        
        if not cls.COHERE_API_KEY:
            errors.append("⚠️ COHERE_API_KEY no está configurada")
        
        if not cls.README_PATH.exists():
            errors.append(f"⚠️ README.md no encontrado en {cls.README_PATH}")
        
        return errors
    
    @classmethod
    def is_valid(cls) -> bool:
        """Retorna True si la configuración es válida."""
        return len(cls.validate()) == 0