import math

def Calcular(num):
    resultDobro = num * 2
    resultTriplo = num * 3
    resultRaiz = math.sqrt(num)

    return resultDobro, resultTriplo, resultRaiz

def MostrarResult(num):
    Dobro, Triplo, Raiz = Calcular(num)

    print(f"O número {num} tem:")
    print(f"Dobro: {Dobro}")
    print(f"Triplo: {Triplo}")
    print(f"Raiz Quadrada: {Raiz}")

numero_digitado = float(input("Informe um número: "))


MostrarResult(numero_digitado)