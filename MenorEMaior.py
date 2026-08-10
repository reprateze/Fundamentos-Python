lista = []


lista = input("Informe 5 numeros separados por vírgula: ")
lista_string = lista.replace(',', ' ').split()

lista_de_numeros = [int(num) for num in lista_string]

NumMax = max(lista_de_numeros)
NumMin = min(lista_de_numeros)


print(F"O maior numero e {NumMax} e o menor e {NumMin}")


