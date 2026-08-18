# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        if n == length:
            return head.next
        
        target = length - n
        curr = head
        prev = None
        while target > 0:
            prev = curr
            curr = curr.next
            target -= 1
        prev.next = curr.next
        return head
        


        