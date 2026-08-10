def CalcularMedia(notas):
    total = sum(notas) / len(notas)
    return total

def PerguntarNotas():
    notas = []
    print("Informe as duas notas a seguir:")

    for i in range(2):
        nota = float(input(f"Nota {i + 1}: "))
        notas.append(nota)
    
    return notas  


notas = PerguntarNotas()          
total = CalcularMedia(notas)     

print(f"Total: {total:.2f}")     
