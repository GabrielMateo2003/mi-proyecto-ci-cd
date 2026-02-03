from app import predecir_inventario

def test_prediccion_logica():
    resultado = predecir_inventario(100)
    # Verificamos que el cálculo sea correcto
    assert resultado == 110
