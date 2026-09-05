def busca_binaria(numeros, alvo):
    esquerda = 0
    direita = len(numeros) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if numeros[meio] == alvo:
            return meio

        elif numeros[meio] < alvo:
            esquerda = meio + 1

        else:
            direita = meio - 1

    return -1


numeros = [1, 3, 5, 7, 9, 11, 13]

print(busca_binaria(numeros, 11))