class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def invert(head):
        atual = head
        aux = None

        while atual:
           nextNode = atual.next
           atual.next = aux
           aux = atual
           atual = nextNode

        return aux

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

print("Antes da inversao:")
printList(aux)

print("Pos inversao:")
printList()