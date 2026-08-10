Frutas = []
quant = int(input("Quantas frutas voce quer registrar?"))

for x in range(quant):
    aux = input("Informe o nome da fruta: ")
    Frutas.append(aux)

print(f"As frutas são: {Frutas}")
print(f"Total de frutas: {len(Frutas)}")

retirar = input("Qual Fruta voce deseja retirar da lista?")

if retirar in Frutas:
        Frutas.remove(retirar)
        print(f"{retirar} foi removida da lista.")
else:
        print("Fruta nao encotrada")

print(f"Lista atualizada: {Frutas}")
