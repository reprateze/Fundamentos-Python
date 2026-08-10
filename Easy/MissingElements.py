import random
from typing import List


class Solution:

    def findMissingElements(self, nums: List[int]) -> List[int]:
        resultado = []

        menor = min(nums)
        maior = max(nums)

        for numero in range(menor, maior + 1):
            if numero not in nums:
                nums.append(numero)
                resultado.append(numero)
        
        nums.sort()

        return nums, resultado
    


def LerVetor():
    vet = input("Informe números separados por vírgula: ")

    numeros = vet.replace(',', ' ').split()

    return [int(num) for num in numeros]


def GeraVetorFaltante(nums):

    copia = nums.copy()

    # pega somente os valores do meio
    candidatos = copia[1:-1]

    # quantidade aleatória de números que serão removidos
    quantidade = random.randint(1, len(candidatos))

    # escolhe vários números aleatórios
    removidos = random.sample(candidatos, quantidade)

    for numero in removidos:
        copia.remove(numero)

    return copia

nums_original = LerVetor()

NumsAux = GeraVetorFaltante(nums_original)

print("Lista original:", nums_original)
print("Lista com número faltando:", NumsAux)

aux = Solution()

resultado, Encontrados = aux.findMissingElements(NumsAux)

print("Lista dos encontrados:", Encontrados)
print("Lista completa novamente:", resultado)
