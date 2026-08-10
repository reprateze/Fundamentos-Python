num = int(input("Informe um número: "))
list_num = []

if num > 0:
    for x in range(1, 11):
        resultado = num * x
        list_num.append((resultado))  # salva (multiplicador, resultado)
else:
    print("Digite um número válido!")


for i, resultado in enumerate(list_num, start=1):
    print(f"{num} x {i} = {resultado}")

