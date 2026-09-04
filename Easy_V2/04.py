
def numero_unico(numeros):    
    contagem = {}

    for numero in numeros:
        if numero in contagem:
            contagem[numero] +=  1 
        else:
            contagem[numero] = 1    


    for numero, qtd in contagem.items():
        if qtd == 1:
            return numero



numeros = [4, 1, 2, 1, 2, 4, 4, 2, 0]

print(numero_unico(numeros))
