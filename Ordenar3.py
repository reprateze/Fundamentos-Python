def imprimir(lista, nome):
    print(f"\n{nome}:")
    for x in lista:
        print(x)

Lista1 = []
ListaPares = []
ListaImpares = []

entrada = input("Informe números separados por espaço: ")
entrada = entrada.replace(',', ' ')  # caso o usuário use vírgulas
valores = entrada.split()

for x in valores:
    num = int(x)
    Lista1.append(num)

    if num % 2 == 0:
        ListaPares.append(num)
    else:
        ListaImpares.append(num)

Lista1.sort()
ListaPares.sort()
ListaImpares.sort()

# Usa a função corrigida
imprimir(Lista1, "Misturado")
imprimir(ListaPares, "Pares")
imprimir(ListaImpares, "Ímpares")

print("\nPrograma finalizado!")
