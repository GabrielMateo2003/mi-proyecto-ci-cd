from app import obtener_precision_modelo

def test_ia_accuracy():
    # Esta función debe existir en tu app.py
    score = obtener_precision_modelo()
    # Verificamos que la IA sea funcional (Accuracy > 0)
    assert score > 0
