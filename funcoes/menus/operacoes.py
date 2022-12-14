import math

def somar(y, z):
    return y + z

def subtrair(y, z):
    return y - z

def multiplicar(y, z):
    return y * z

def dividir(y, z):
    try:
        division = y / z
    except ZeroDivisionError:
        print("Não é possível dividir por zero")
    else:
        return round(y / z, 0)

def potencia(y, z):
    return y ** z

def raiz(z):
    return round(z ** 0.5, 0)

def fatorial(x):
    return math.factorial(x)