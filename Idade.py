from datetime import datetime

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))


data_atual = datetime.now().year
ano_100 = data_atual + (100 -idade)


print(f"Olá, {nome} em {ano_100} você fará 100 anos!")