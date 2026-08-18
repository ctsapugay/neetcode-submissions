# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1
        
        result = dummy = ListNode(0, None)
        list1 = head1
        list2 = head2
        
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                result = result.next
                list1 = list1.next
            else:
                result.next = list2
                result = result.next
                list2 = list2.next

        if list1:
            result.next = list1
        else:
            result.next = list2
        
        return dummy.next