def two_sum(numeros, alvo):
    vistos = {}

    for i, numero in enumerate(numeros):
        aux = alvo - numero
        if aux not in vistos:
           vistos[numero] = i
        else:
            return [vistos[aux], i]
            

         
numeros = [2, 11, 7, 15]

print(two_sum(numeros, 9))