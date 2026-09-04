def two_sum(numeros, alvo):
    esquerda = 0
    direita = len(numeros) - 1

    while esquerda < direita:
        soma = numeros[esquerda] + numeros[direita]

        if soma == alvo:
            return [esquerda, direita]

        elif soma < alvo:
            esquerda += 1

        else:
            direita -= 1

    return []