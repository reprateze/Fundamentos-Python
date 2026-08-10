nums = []

nums = input("Informe 5 numeros separados por vírgula: ")
nums_string = nums.replace(',', ' ').split()

NumResult = [int(num) for num in nums_string]

target = int(input("Informe o valor a ser procurado:"))

mapa = {}

for i, num in enumerate(NumResult):
    complemento = target - num

    if complemento in mapa:
        print(mapa[complemento], i)
        break   
    
    mapa[num] = i

