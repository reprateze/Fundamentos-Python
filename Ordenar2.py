num = []

for x in range(10):
    valor = int(input(f"Informe o {x+1}° número da lista: "))
    num.append(valor)

# Ordena depois de todos os valores serem inseridos
num.sort()

# Imprime os números em ordem crescente
print("\nNúmeros em ordem crescente:")
for x in num:
    print(x)

print("_________________________")

maior = max(num)
menor = min(num)

print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
