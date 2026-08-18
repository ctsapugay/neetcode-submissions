# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            curr = list1
            head = list1
            pt1 = list1.next
            pt2 = list2
        else:
            curr = list2
            head = list2
            pt1 = list1
            pt2 = list2.next
        
        while pt1 is not None and pt2 is not None:
            if pt1.val < pt2.val:
                curr.next = pt1
                pt1 = pt1.next
            else:
                curr.next = pt2
                pt2 = pt2.next
            curr = curr.next
        
        if pt1 is None:
            curr.next = pt2
        else:
            curr.next = pt1
        
        return head
        