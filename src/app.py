"""
Aplicación principal del sistema RAG con Streamlit y Cohere.
"""
import streamlit as st
import sys
from pathlib import Path

# Agregar el directorio src al path
sys.path.insert(0, str(Path(__file__).parent))

from components.chat_interface import ChatInterface
from components.sidebar import render_sidebar
from services.rag_service import RAGService
from utils.config import Config


def main():
    """Función principal de la aplicación."""
    
    # Configuración de la página
    st.set_page_config(
        page_title="Cerebro y Código - RAG",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Validar configuración
    config_errors = Config.validate()
    
    if config_errors:
        st.error("❌ Error de configuración")
        for error in config_errors:
            st.warning(error)
        
        st.info("""
        ### 📝 Pasos para configurar:
        
        1. **Obtén una API key de Cohere:**
           - Ve a https://dashboard.cohere.com/api-keys
           - Crea una cuenta gratuita si no la tienes
           - Copia tu API key
        
        2. **Crea un archivo .env en el directorio raíz:**
           ```
           COHERE_API_KEY=tu-api-key-aqui
           ```
        
        3. **Verifica que existe el archivo README.md en la carpeta data/**
        
        4. **Reinicia la aplicación**
        """)
        
        st.stop()
    
    # Inicializar el servicio RAG (solo una vez por sesión)
    if "rag_service" not in st.session_state:
        with st.spinner("🔄 Inicializando sistema RAG... Esto puede tomar unos segundos."):
            try:
                st.session_state.rag_service = RAGService(
                    api_key=Config.COHERE_API_KEY,
                    data_path=str(Config.README_PATH)
                )
                st.success("✅ Sistema RAG inicializado correctamente")
            except Exception as e:
                st.error(f"❌ Error al inicializar el sistema RAG: {str(e)}")
                st.stop()
    
    # Renderizar sidebar
    num_messages = len(st.session_state.get("messages", []))
    render_sidebar(num_messages)
    
    # Renderizar interfaz de chat
    chat_interface = ChatInterface(st.session_state.rag_service)
    chat_interface.render()
    
    # Footer
    st.divider()
    st.caption("💡 Desarrollado con Streamlit, Cohere, LangChain y ChromaDB | 📦 Cerebro y Código © 2025")


if __name__ == "__main__":
    main()