def VerificaNum(num):
    antecessor = num - 1
    sucessor = num + 1
    
    return sucessor, antecessor

def MostrarResultado(num):
    
    sucessor, antecessor = VerificaNum(num)
    
    
    print(f"O número selecionado {num} possui o sucessor {sucessor} e o antecessor {antecessor}.")


print("Informe um numero:")

selecionado = int(input())

# Chama a função MostrarResultado e passa o número digitado como argumento.
MostrarResultado(selecionado)