# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l, r = dummy, head

        for i in range(n-1):
            r = r.next

        while r.next:
            l = l.next
            r = r.next
        
        if l == dummy:
            return head.next
        
        l.next = l.next.next
        return head

