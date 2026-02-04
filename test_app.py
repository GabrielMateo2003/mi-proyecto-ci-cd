from app import entrenar_y_validar

def test_modelo_ia():
    # La prueba invoca la función y verifica que la precisión sea razonable
    accuracy = entrenar_y_validar()
    assert accuracy > 0.60  # El modelo debe ser mejor que el azar
