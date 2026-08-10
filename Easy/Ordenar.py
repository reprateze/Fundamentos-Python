Frutas = []
quant = int(input("Quantas frutas voce quer registrar? "))

for x in range(quant):
    aux = input("Informe o nome da fruta: ")
    Frutas.append(aux)

print(f"As frutas são: {Frutas}")
print(f"Total de frutas: {len(Frutas)}")

procura = input("Informe o valor procurado: ")

indice = Frutas.index(procura)
print(f"{procura} esta no indice {indice}")