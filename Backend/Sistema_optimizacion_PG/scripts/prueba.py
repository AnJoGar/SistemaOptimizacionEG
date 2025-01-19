import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
import random
# Cargar el archivo con los datos preprocesados
with open('preprocessed_data_with_responses.pkl', 'rb') as f:
    preprocessed_data = pickle.load(f)

# Cargar el modelo entrenado
with open('random_forest_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Recuperar el vectorizador, el codificador de etiquetas y el mapa de respuestas
vectorizer = preprocessed_data['vectorizer']
label_encoder = preprocessed_data['label_encoder']
response_map = preprocessed_data['response_map']

def predict_intent(text):
    # Preprocesar el texto de entrada (igual que durante el entrenamiento)
    text = text.lower()  # Convertir a minúsculas
    text = ''.join([char for char in text if char.isalnum() or char.isspace()])  # Eliminar puntuación
    
    # Vectorizar el texto
    text_vec = vectorizer.transform([text])
    
    # Realizar la predicción
    prediction = model.predict(text_vec)
    
    # Decodificar la predicción (convertir el número a la intención correspondiente)
    intent = label_encoder.inverse_transform(prediction)
    
    # Recuperar las posibles respuestas para la intención predicha
    responses = response_map.get(intent[0], ["Lo siento, no entiendo esa pregunta."])
    
    return intent[0], random.choice(responses)  # Elegir una respuesta aleatoria

# Ejemplo de prueba
print("Prueba de chat con el modelo entrenado\n")

while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        print("Bot: Adiós!")
        break
    
    intent, response = predict_intent(user_input)
    print(f"Bot (Intención: {intent}): {response}")
