# tests/test_calculadora.py
import pytest
from SRC.calculadora import somar, dividir, multiplicar, subtrair 

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_multiplicar():
    assert multiplicar(2, 5) == 10
    assert multiplicar(4, 1) == 4

def test_subtrair():
    assert subtrair(6, 2) == 4
    with pytest.raises(ValueError):
        subtrair(4, 9)