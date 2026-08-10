class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def printList(head):
    atual = head
    while atual:
        print(atual.val)
        atual = atual.next  


aux = Node(10)
aux2 = Node(20)
aux3 = Node(30)

aux.next = aux2
aux2.next = aux3

# 5. Chamar a função passando o primeiro nó ("head" ou "cabeça" da lista)
print("\nValores da lista:")
printList(aux)