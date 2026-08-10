
lista = []
entrada = input("Informe 5 numeros separados por vírgula: ")
lista_string = entrada.replace(',', ' ').split()

# Pede um número para ser procurado
Num = input("Informe um numero para ser procurado: ")

# Itera sobre a lista para procurar o número
if Num in lista_string:
    print(f"O número {Num} está na lista.")
else:
    print(f"O número {Num} não está na lista.")

print(lista_string)