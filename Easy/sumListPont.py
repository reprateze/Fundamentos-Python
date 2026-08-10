class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sumlist(head):
    atual = head
    total = 0

    while atual:
        total += atual.val
        atual = atual.next

    return total


# criando a lista
aux = Node(10)
aux2 = Node(20)
aux3 = Node(30)

aux.next = aux2
aux2.next = aux3

print(sumlist(aux))