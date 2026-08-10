idade = int(input("Informe sua idade para verificação: "))

if idade <= 12:
    print("Criança!!")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")
