alunos = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 5.0},
    {"nome": "Carlos", "nota": 9.2},
    {"nome": "Diana", "nota": 6.0},
    {"nome": "Eduardo", "nota": 4.5}
]

aprovados = list(filter(lambda x: x["nota"]>=6, alunos))
nomes = list(map(lambda x: x["nome"], aprovados))

print(nomes)