import json
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import random
# Cargar el dataset JSON
with open('../data/data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Verificar si se cargó correctamente el JSON
print("Contenido completo del JSON:")
print(json.dumps(data, indent=2))  # Imprime el JSON de manera más legible

# Convertir el dataset a un DataFrame
data_records = []
response_map = {}  # Mapeo de intenciones a respuestas

for item in data:
    print(f"Procesando intención: {item['intent']}")
    for example in item['examples']:
        data_records.append({
            'texto': example,
            'intencion': item['intent']
        })
    
    # Guardar las respuestas para cada intención
    response_map[item['intent']] = item['responses']

# Crear el DataFrame
df = pd.DataFrame(data_records)

# Preprocesar el texto (limpieza de texto, tokenización, etc.)
df['texto'] = df['texto'].str.lower()  # Convertir todo a minúsculas
df['texto'] = df['texto'].str.replace(r'[^\w\s]', '', regex=True)  # Eliminar puntuación

# División de los datos en características (X) y etiquetas (y)
X = df['texto']
y = df['intencion']

# Dividir el conjunto de datos en entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorización del texto (Convertir texto a una representación numérica)
vectorizer = CountVectorizer(stop_words='english')  # Eliminamos las palabras comunes (stopwords)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Etiquetado de las intenciones (convertirlas a números)
label_encoder = LabelEncoder()
y_train_encoded = label_encoder.fit_transform(y_train)
y_test_encoded = label_encoder.transform(y_test)

# Guardar los datos preprocesados en un archivo pickle
preprocessed_data = {
    'X_train': X_train_vec,
    'X_test': X_test_vec,
    'y_train': y_train_encoded,
    'y_test': y_test_encoded,
    'vectorizer': vectorizer,
    'label_encoder': label_encoder,
    'response_map': response_map  # Guardamos el mapa de respuestas
}

# Guardar los datos procesados en un archivo .pkl
with open('preprocessed_data_with_responses.pkl', 'wb') as f:
    pickle.dump(preprocessed_data, f)

# Crear y entrenar el modelo de Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrenar el modelo
model.fit(X_train_vec, y_train_encoded)

# Realizar predicciones
y_pred = model.predict(X_test_vec)

# Evaluar el modelo
accuracy = accuracy_score(y_test_encoded, y_pred)
print(f"\nPrecisión del modelo: {accuracy * 100:.2f}%")

# Reporte completo de clasificación
print("\nReporte de clasificación:\n")
print(classification_report(y_test_encoded, y_pred))

# Guardar el modelo entrenado en un archivo
with open('random_forest_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Modelo entrenado y guardado correctamente en 'random_forest_model.pkl'.")

