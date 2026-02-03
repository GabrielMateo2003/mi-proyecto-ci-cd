from app import predecir_inventario
import pytest

def test_prediccion_logica():
    resultado = predecir_inventario(100)
    # Usamos approx para ignorar esos mini decimales de error
    assert resultado == pytest.approx(110)
