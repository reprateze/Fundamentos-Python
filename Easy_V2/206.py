from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        proximo = None
        atual = head
        anterior = None

        while atual:
            proximo = atual.next
            atual.next = anterior
            anterior = atual
            atual = proximo

        return anterior
           

        
    

       