def find_iguais(numeros):
    vistos = {}

    for numero in numeros:
        if numero in vistos:
            print("Repetido:", numero)
        else:
            vistos[numero] = True


num = [1, 2, 3, 2, 4, 1, 5]

find_iguais(num)