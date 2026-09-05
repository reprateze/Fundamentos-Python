def maior_soma(numeros, k):
    janela = sum(numeros[:k])
    maior = janela

    for direita in range(k, len(numeros)):
        janela = janela - numeros[direita - k ] + numeros[direita]
        maior = max(maior, janela)

