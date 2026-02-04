from app import obtener_precision_modelo

def test_calidad_modelo():
    precision = obtener_precision_modelo()
    # Verificamos que el modelo de IA tenga una precisión mínima aceptable (ej. 70%)
    assert precision > 0.70
