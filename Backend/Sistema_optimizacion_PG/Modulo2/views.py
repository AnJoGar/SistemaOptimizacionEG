from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import pickle
import random
from django.conf import settings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder

class ChatbotAPI(APIView):
    def post(self, request, *args, **kwargs):
        # Obtener el input del usuario del cuerpo de la solicitud
        user_input = request.data.get("mensaje", "")
        
        if not user_input:
            return Response({"error": "No input provided."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Ruta al archivo del modelo y datos
        modelo_path = os.path.join(settings.BASE_DIR, 'scripts/random_forest_model.pkl')
        
        # Cargar el archivo con los datos preprocesados
        with open(os.path.join(settings.BASE_DIR, 'scripts/preprocessed_data_with_responses.pkl'), 'rb') as f:
            preprocessed_data = pickle.load(f)

        # Cargar el modelo entrenado
        with open(modelo_path, 'rb') as f:
            model = pickle.load(f)

        # Recuperar el vectorizador, el codificador de etiquetas y el mapa de respuestas
        vectorizer = preprocessed_data['vectorizer']
        label_encoder = preprocessed_data['label_encoder']
        response_map = preprocessed_data['response_map']
        
        # Preprocesar el texto de entrada (igual que durante el entrenamiento)
        text = user_input.lower()  # Convertir a minúsculas
        text = ''.join([char for char in text if char.isalnum() or char.isspace()])  # Eliminar puntuación
        
        # Vectorizar el texto
        text_vec = vectorizer.transform([text])
        
        # Realizar la predicción
        prediction = model.predict(text_vec)
        
        # Decodificar la predicción (convertir el número a la intención correspondiente)
        intent = label_encoder.inverse_transform(prediction)
        
        # Recuperar las posibles respuestas para la intención predicha
        responses = response_map.get(intent[0], ["Lo siento, no entiendo esa pregunta."])
        
        # Responder con la intención y una respuesta aleatoria
        response_data = {
            "intent": intent[0],
            "response": random.choice(responses)
        }
        
        return Response(response_data, status=status.HTTP_200_OK)
