import pandas as pd
import numpy as np

# Generar un dataset simulado similar al anterior
np.random.seed(42)

# Número de muestras
n_samples = 100

# Datos simulados
data = {
    "user_id": np.arange(1, n_samples + 1),
    "age": np.random.randint(18, 60, size=n_samples),
    "gender": np.random.choice(["Male", "Female"], size=n_samples),
    "location": np.random.choice(["Urban", "Rural"], size=n_samples),
    "interaction_frequency": np.random.randint(1, 30, size=n_samples),
    "preferred_service": np.random.choice([1, 2, 3, 4, 5], size=n_samples),  # Servicios en Ecuador
    "activity_level": np.random.choice(["Low", "Medium", "High"], size=n_samples),
    "feedback_provided": np.random.choice([0, 1], size=n_samples),  # 0 = No, 1 = Sí
}

# Crear DataFrame
dataset = pd.DataFrame(data)

# Actualizar la columna 'preferred_service' con servicios más realistas
dataset["preferred_service"] = dataset["preferred_service"].map({
    1: "Registro Civil",
    2: "SRI",
    3: "ANT",
    4: "IESS",
    5: "Municipalidad"
})

# Guardar el dataset actualizado en un archivo CSV
dataset.to_csv('simulated_user_segmentation_dataset_ecuador_services.csv', index=False)

print("Dataset generado y guardado como 'simulated_user_segmentation_dataset_ecuador_services.csv'")
