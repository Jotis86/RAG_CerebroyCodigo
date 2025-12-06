import streamlit as st


def render_sidebar(num_messages: int = 0):
    """
    Renderiza el sidebar con información y estadísticas.
    
    Args:
        num_messages: Número de mensajes en la conversación
    """
    st.sidebar.title("⚙️ Configuración")
    
    # Información del sistema
    st.sidebar.markdown("### 📊 Estadísticas")
    st.sidebar.metric("Mensajes en conversación", num_messages)
    
    st.sidebar.divider()
    
    # Información sobre el asistente
    st.sidebar.markdown("### ℹ️ Sobre este asistente")
    st.sidebar.info("""
    Este asistente utiliza **RAG** (Retrieval-Augmented Generation) para responder 
    preguntas basándose en el contenido del repositorio **Cerebro y Código**.
    
    **Tecnologías usadas:**
    - Cohere API (LLM)
    - ChromaDB (Vector Store)
    - LangChain (Orquestación)
    - Streamlit (Interfaz)
    """)
    
    st.sidebar.divider()
    
    # Enlaces útiles
    st.sidebar.markdown("### 🔗 Enlaces útiles")
    st.sidebar.markdown("""
    - 📦 [GitHub Repo](https://github.com/Jotis86/CerebroyCodigo)
    - 📧 [Contacto](mailto:jotaduranbon@gmail.com)
    """)
    
    st.sidebar.divider()
    
    # Configuración técnica
    st.sidebar.markdown("### 🔧 Configuración técnica")
    with st.sidebar.expander("Ver detalles"):
        st.caption("**Modelo LLM:** command-r7b-12-2024")
        st.caption("**Embeddings:** embed-multilingual-v3.0")
        st.caption("**Vector DB:** ChromaDB")
        st.caption("**Chunk size:** 1000 tokens")
        st.caption("**Overlap:** 200 tokens")
        st.caption("**Top-k retrieval:** 4 documentos")
    
    st.sidebar.divider()
    
    # Ayuda
    st.sidebar.markdown("### 💡 Consejos de uso")
    with st.sidebar.expander("¿Cómo usar el asistente?"):
        st.markdown("""
        1. **Haz preguntas específicas** sobre recursos, tecnologías o rutas de aprendizaje
        2. **Usa las preguntas sugeridas** si no sabes por dónde empezar
        3. **Activa "Mostrar fuentes"** para ver de dónde viene la información
        4. **Limpia el chat** cuando quieras empezar una nueva conversación
        
        **Ejemplos de preguntas:**
        - ¿Qué recursos hay para aprender Python?
        - ¿Cómo puedo empezar con Machine Learning?
        - ¿Qué herramientas recomiendas para análisis de datos?
        """)
    
    return None