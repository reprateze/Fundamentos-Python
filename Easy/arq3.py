with open("alunos.txt", "r") as arq:
    linhas = arq.readlines()

for linha in linhas:
    partes = linha.strip().split()

    nome = partes[0]
    notas = list(map(int, partes[1:]))

    media = sum(notas) / len(notas)
    minimo = min(notas)
    maximo = max(notas)

    print("Aluno:", nome)
    print("Media:", media)
    print("Min:", minimo)
    print("Max:", maximo)
    print("-" * 20)