import streamlit as st
from services.rag_service import RAGService
from utils.config import Config
import os


class ChatInterface:
    """Interfaz de chat mejorada con sistema RAG."""
    
    def __init__(self, rag_service: RAGService):
        """
        Inicializa la interfaz de chat.
        
        Args:
            rag_service: Servicio RAG para responder preguntas
        """
        self.rag_service = rag_service
        
        # Inicializar el estado de sesión si no existe
        if "messages" not in st.session_state:
            st.session_state.messages = []
        
        if "show_sources" not in st.session_state:
            st.session_state.show_sources = True
    
    def render(self):
        """Renderiza la interfaz de chat."""
        
        # Título y descripción
        st.title("🧠 Cerebro y Código - Asistente RAG")
        st.markdown("""
        ¡Hola! Soy tu asistente virtual del repositorio **Cerebro y Código**. 
        Pregúntame sobre cualquier recurso, ruta de aprendizaje o tecnología disponible en el repositorio.
        """)
        
        # Columnas para opciones
        col1, col2 = st.columns([3, 1])
        with col2:
            if st.button("🗑️ Limpiar Chat"):
                st.session_state.messages = []
                st.rerun()
        
        # Checkbox para mostrar fuentes
        st.session_state.show_sources = st.checkbox(
            "📚 Mostrar fuentes de información",
            value=st.session_state.show_sources
        )
        
        st.divider()
        
        # Mostrar preguntas sugeridas si no hay mensajes
        if len(st.session_state.messages) == 0:
            st.markdown("### 💡 Preguntas sugeridas:")
            suggested = self.rag_service.get_suggested_questions()
            
            cols = st.columns(2)
            for idx, question in enumerate(suggested):
                col_idx = idx % 2
                with cols[col_idx]:
                    if st.button(f"❓ {question}", key=f"sugg_{idx}"):
                        self._process_question(question)
                        st.rerun()
        
        # Mostrar historial de mensajes
        for message in st.session_state.messages:
            self._render_message(message)
        
        # Input del usuario
        with st.container():
            user_input = st.chat_input("Escribe tu pregunta aquí...")
            
            if user_input:
                self._process_question(user_input)
                st.rerun()
    
    def _process_question(self, question: str):
        """
        Procesa una pregunta del usuario.
        
        Args:
            question: Pregunta del usuario
        """
        # Agregar pregunta del usuario al historial
        st.session_state.messages.append({
            "role": "user",
            "content": question
        })
        
        # Obtener respuesta del RAG
        with st.spinner("🔍 Buscando información..."):
            response = self.rag_service.answer_question(question)
        
        # Agregar respuesta al historial
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["answer"],
            "sources": response.get("sources", []),
            "scores": response.get("similarity_scores", [])
        })
    
    def _render_message(self, message: dict):
        """
        Renderiza un mensaje en el chat.
        
        Args:
            message: Diccionario con información del mensaje
        """
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
            # Mostrar fuentes si es una respuesta del asistente
            if message["role"] == "assistant" and st.session_state.show_sources:
                sources = message.get("sources", [])
                if sources:
                    with st.expander("📚 Ver fuentes utilizadas"):
                        for idx, source in enumerate(sources):
                            st.markdown(f"**Fuente {idx + 1}:**")
                            st.text(source["content"])
                            st.caption(f"Chunk: {source['metadata'].get('chunk', 'N/A')}")
                            st.divider()
    
    def render_sidebar_info(self):
        """Renderiza información adicional en el sidebar."""
        st.sidebar.markdown("### 📊 Estadísticas")
        st.sidebar.metric(
            "Mensajes en la conversación",
            len(st.session_state.messages)
        )
        
        st.sidebar.markdown("### ℹ️ Sobre este asistente")
        st.sidebar.info("""
        Este asistente utiliza **RAG (Retrieval-Augmented Generation)** para responder 
        preguntas basándose en el contenido del repositorio Cerebro y Código.
        
        **Tecnologías:**
        - Cohere API (LLM)
        - ChromaDB (Vector Store)
        - LangChain (Orquestación)
        - Streamlit (Interfaz)
        """)
        
        st.sidebar.markdown("### 🔗 Enlaces")
        st.sidebar.markdown("""
        - [GitHub Repo](https://github.com/Jotis86/CerebroyCodigo)
        """)
        
        st.sidebar.markdown("### ⚙️ Configuración")
        st.sidebar.caption(f"Modelo: command-r7b-12-2024")
        st.sidebar.caption(f"Embeddings: embed-multilingual-v3.0")