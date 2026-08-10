# ----------------------
# 1. ESCREVENDO NO ARQUIVO
# ----------------------

with open("carros.txt", "w") as arq:
    lista = ["Uno\n", "Gol\n", "Up\n", "Ka\n", "Fusca\n"]
    arq.writelines(lista)


# ----------------------
# 2. LENDO O ARQUIVO
# ----------------------

with open("carros.txt", "r") as arq:
    linhas = arq.readlines()


# ----------------------
# 3. MOSTRANDO TODOS
# ----------------------

print("Todos os carros:")
for linha in linhas:
    print(linha.strip())


# ----------------------
# 4. FILTRANDO (4 letras)
# ----------------------

print("\nCarros com 4 letras:")

encontrou = False

for linha in linhas:
    nome = linha.strip()
    
    if len(nome) == 4:
        print(nome)
        encontrou = True

if not encontrou:
    print("Nenhum encontrado")