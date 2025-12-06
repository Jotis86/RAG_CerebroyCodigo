import os
from typing import List, Dict, Tuple
import cohere
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_cohere import CohereEmbeddings
from langchain_core.documents import Document
from utils.config import Config


class RAGService:
    """
    Servicio RAG (Retrieval-Augmented Generation) para responder preguntas
    basadas en el contenido del README.
    """
    
    def __init__(self, api_key: str, data_path: str):
        """
        Inicializa el servicio RAG.
        
        Args:
            api_key: API key de Cohere
            data_path: Ruta al archivo README.md
        """
        self.api_key = api_key
        self.data_path = data_path
        self.cohere_client = cohere.Client(api_key)
        self.embeddings = CohereEmbeddings(
            cohere_api_key=api_key,
            model="embed-multilingual-v3.0"
        )
        self.vectorstore = None
        self.documents = []
        
        # Inicializar el vectorstore con los documentos
        self._load_and_index_documents()
    
    def _load_and_index_documents(self):
        """Carga el README y crea el índice vectorial."""
        try:
            # Leer el archivo README
            with open(self.data_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Dividir el texto en chunks manejables
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                separators=["\n## ", "\n### ", "\n---", "\n\n", "\n", " ", ""]
            )
            
            # Crear documentos
            chunks = text_splitter.split_text(content)
            self.documents = [
                Document(page_content=chunk, metadata={"source": "README.md", "chunk": i})
                for i, chunk in enumerate(chunks)
            ]
            
            # Crear vectorstore con ChromaDB
            self.vectorstore = Chroma.from_documents(
                documents=self.documents,
                embedding=self.embeddings,
                collection_name="cerebro_y_codigo"
            )
            
            print(f"✅ Documentos cargados: {len(self.documents)} chunks indexados")
            
        except Exception as e:
            print(f"❌ Error al cargar documentos: {str(e)}")
            raise
    
    def retrieve_context(self, query: str, k: int = 4) -> List[Tuple[Document, float]]:
        """
        Recupera los documentos más relevantes para una consulta.
        
        Args:
            query: Pregunta del usuario
            k: Número de documentos a recuperar
            
        Returns:
            Lista de tuplas (documento, score de similitud)
        """
        if not self.vectorstore:
            raise ValueError("Vectorstore no inicializado")
        
        # Búsqueda de similitud
        results = self.vectorstore.similarity_search_with_score(query, k=k)
        return results
    
    def generate_answer(self, query: str, context_docs: List[Document]) -> Dict:
        """
        Genera una respuesta usando Cohere con el contexto recuperado.
        
        Args:
            query: Pregunta del usuario
            context_docs: Documentos recuperados como contexto
            
        Returns:
            Diccionario con la respuesta y metadatos
        """
        # Construir el contexto
        context = "\n\n".join([doc.page_content for doc in context_docs])
        
        # Crear el prompt para Cohere
        prompt = f"""Eres un asistente experto y amigable en tecnología y programación para el repositorio educativo "Cerebro y Código" (https://github.com/Jotis86/CerebroyCodigo). 

CONTEXTO DISPONIBLE:
{context}

PREGUNTA DEL USUARIO: {query}

INSTRUCCIONES IMPORTANTES:

1. **Para saludos, agradecimientos o conversación casual:**
   - Responde de manera amigable y natural
   - Preséntate como el asistente de "Cerebro y Código"
   - Ofrece ayuda o pregunta en qué puedes asistir
   - Puedes mencionar que tienes acceso a recursos del repositorio de GitHub
   - No menciones la falta de contexto

2. **Para preguntas técnicas sobre recursos, tecnologías o aprendizaje:**
   - Responde BASÁNDOTE en el contexto proporcionado
   - **MUY IMPORTANTE:** Convierte TODAS las rutas de recursos a enlaces completos de GitHub
   - Para PDFs del repositorio, usa este formato EXACTO: https://github.com/Jotis86/CerebroyCodigo/blob/main/[carpeta]/[archivo].pdf
   - Ejemplo: "./1_Fundamentos/Python.pdf" se convierte en "https://github.com/Jotis86/CerebroyCodigo/blob/main/1_Fundamentos/Python.pdf"
   - Los enlaces externos (exercism.org, kaggle.com, etc.) mantenlos tal cual
   - CADA recurso del repo DEBE tener su propio enlace clickeable individual
   - Formatea como: [Nombre descriptivo](URL_completa)
   - Sé específico y útil con la información disponible
   - Si la pregunta no puede responderse con el contexto, di: "No encontré información específica sobre eso en los recursos disponibles, pero puedo ayudarte con otros temas del repositorio"

3. **Formato de respuesta para recursos:**
   - Lista TODOS los recursos con viñetas
   - CADA recurso PDF debe tener formato: "📚 [Nombre](https://github.com/Jotis86/CerebroyCodigo/blob/main/carpeta/archivo.pdf)"
   - Enlaces externos: "🔗 [Nombre](URL_externa)"
   - Ejemplo correcto: "📚 [Python general](https://github.com/Jotis86/CerebroyCodigo/blob/main/1_Fundamentos/Python.pdf)"
   - Ejemplo correcto externo: "🔗 [Exercism](https://exercism.org/)"
   - Agrupa recursos por categoría cuando sea apropiado
   - USA SIEMPRE "/blob/main/" en las URLs (NO "/raw/main/")
   - Al hacer click, GitHub mostrará el archivo con un botón "Download"

4. **Estilo de respuesta:**
   - Sé claro, conciso y útil
   - Responde siempre en español
   - Mantén un tono profesional pero amigable
   - Si es apropiado, sugiere preguntas relacionadas
   - Usa emojis ocasionalmente para hacer la respuesta más visual (📚 🔗 💡 🎯 ✨)

RESPUESTA:"""
        
        try:
            # Generar respuesta con Cohere (v5.x API)
            response = self.cohere_client.chat(
                message=prompt,
                model=Config.LLM_MODEL,
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS,
            )
            
            # En Cohere v5.x, la respuesta puede estar en response.text o response.message
            answer = response.text if hasattr(response, 'text') else (
                response.message if hasattr(response, 'message') else str(response)
            )
            
            return {
                "answer": answer,
                "sources": [
                    {
                        "content": doc.page_content[:200] + "...",
                        "metadata": doc.metadata
                    }
                    for doc in context_docs
                ]
            }
            
        except Exception as e:
            print(f"❌ Error al generar respuesta: {str(e)}")
            return {
                "answer": f"Lo siento, ocurrió un error al generar la respuesta: {str(e)}",
                "sources": []
            }
    
    def answer_question(self, query: str) -> Dict:
        """
        Método principal: responde una pregunta usando RAG.
        
        Args:
            query: Pregunta del usuario
            
        Returns:
            Diccionario con respuesta y fuentes
        """
        try:
            # 1. Recuperar contexto relevante
            results = self.retrieve_context(query, k=4)
            context_docs = [doc for doc, score in results]
            
            # 2. Generar respuesta con el contexto
            response = self.generate_answer(query, context_docs)
            
            # 3. Agregar scores de similitud
            response["similarity_scores"] = [float(score) for doc, score in results]
            
            return response
            
        except Exception as e:
            print(f"❌ Error en answer_question: {str(e)}")
            return {
                "answer": f"Lo siento, ocurrió un error: {str(e)}",
                "sources": [],
                "similarity_scores": []
            }
    
    def get_suggested_questions(self) -> List[str]:
        """Retorna preguntas sugeridas para el usuario."""
        return [
            "¿Qué recursos hay disponibles para aprender Python?",
            "¿Cómo puedo aprender Machine Learning?",
            "¿Qué herramientas recomiendas para análisis de datos?",
            "¿Cuáles son las rutas de aprendizaje disponibles?",
            "¿Dónde puedo practicar SQL?",
            "¿Qué recursos hay sobre bases de datos?",
            "¿Cómo puedo desplegar aplicaciones con Streamlit?",
            "¿Qué es RAG y cómo se usa?"
        ]

