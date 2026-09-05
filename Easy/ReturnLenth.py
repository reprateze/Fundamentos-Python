def Contador(*args):
    return len(args)


print("Lembre-se, sempre separado por virgula")
entrada = input("Informe quantos valores vc desejar para serem contabilizados:")

aux = entrada.split(",")


print(Contador(*aux))