def Consulta_ordem(order,friends):
    aux = []
    for i in order:
        if i in friends:
            aux.append(i)

    return aux

order = [3, 1, 5, 2, 4]
friends = [1, 4]

print(Consulta_ordem(order, friends))