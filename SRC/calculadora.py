def somar (a, b):
    return a + b

def dividir (a, b):
    if b == 0:
        raise ValueError("Divisão por Zero!")
    return a / b