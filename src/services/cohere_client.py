import cohere
from typing import List, Dict
from utils.config import Config


class CohereClient:
    """Cliente actualizado para la API de Cohere."""
    
    def __init__(self, api_key: str):
        """
        Inicializa el cliente de Cohere.
        
        Args:
            api_key: API key de Cohere
        """
        self.api_key = api_key
        self.client = cohere.Client(api_key)
    
    def send_message(
        self,
        message: str,
        chat_history: List[Dict] = None,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> Dict:
        """
        Envía un mensaje a Cohere y obtiene la respuesta.
        
        Args:
            message: Mensaje del usuario
            chat_history: Historial de chat previo
            temperature: Temperatura para la generación
            max_tokens: Máximo de tokens en la respuesta
            
        Returns:
            Diccionario con la respuesta
        """
        try:
            response = self.client.chat(
                message=message,
                chat_history=chat_history or [],
                model=Config.LLM_MODEL,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            
            return {
                "text": response.text,
                "success": True,
                "conversation_id": response.conversation_id if hasattr(response, 'conversation_id') else None
            }
            
        except Exception as e:
            return {
                "text": f"Error al comunicarse con Cohere: {str(e)}",
                "success": False,
                "conversation_id": None
            }
    
    def generate_text(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 500
    ) -> str:
        """
        Genera texto basado en un prompt.
        
        Args:
            prompt: Prompt para generar texto
            temperature: Temperatura para la generación
            max_tokens: Máximo de tokens
            
        Returns:
            Texto generado
        """
        try:
            response = self.client.generate(
                prompt=prompt,
                model=Config.LLM_MODEL,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            
            return response.generations[0].text
            
        except Exception as e:
            return f"Error: {str(e)}"