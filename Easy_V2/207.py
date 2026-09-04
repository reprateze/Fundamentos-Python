from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def List(self, head: Optional[ListNode]) -> Optional[ListNode]:

        while head:
            print(head.val)
            head = head.next


no3 = ListNode(3)
no2 = ListNode(2, no3)
no1 = ListNode(1, no2)

s = Solution()
s.List(no1)