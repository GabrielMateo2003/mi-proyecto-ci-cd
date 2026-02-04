1. Contexto del Proyecto
Este proyecto implementa un flujo de Integración Continua (CI) utilizando GitHub Actions para automatizar la validación de modelos de Machine Learning. El caso de estudio se centra en la clasificación de datos del dataset "Affairs", comparando modelos de Regresión Logística, Árboles de Decisión y Random Forest para asegurar la mejor precisión en las predicciones.

2. Funcionalidad del Flujo CI/CD
El flujo automatizado garantiza que cualquier cambio en el código sea validado técnicamente antes de considerarse funcional:

Instalación Automática: Configura un entorno de Python 3.10 e instala las dependencias necesarias (pandas, scikit-learn, numpy).

Entrenamiento y Evaluación: Ejecuta el script de IA (app.py), entrena los modelos y genera métricas de desempeño.

Pruebas de Calidad (Unit Testing): Mediante pytest, el sistema verifica que la precisión (Accuracy) del modelo sea superior al 60%, asegurando que el modelo sea estadísticamente relevante.

3. Tecnologías Utilizadas
Lenguaje: Python 3.10.

Automatización: GitHub Actions.

IA & Data Science: Scikit-learn, Pandas, Numpy.

Testing: Pytest.
