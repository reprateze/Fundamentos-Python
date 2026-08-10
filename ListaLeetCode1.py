vet = ['pare','desktop','tio','pote']

encontrou = False

for palavra in vet:
    if len(palavra) == 4:
        print(palavra)
        encontrou = True

if not encontrou:
    print("Nada para printar")