id="w3"
# escrevendo
with open("numeros.txt", "w") as arq:
    for i in range(5):
        arq.write(str(i) + "\n")

# lendo
with open("numeros.txt", "r") as arq:
    for linha in arq:
        print("Numero:", linha.strip())