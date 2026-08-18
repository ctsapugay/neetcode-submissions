# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge2Lists(self, head1: ListNode, head2: ListNode):
        result = dummy = ListNode(0, None)
        list1 = head1
        list2 = head2
        
        while list1 and list2:
            if list1.val < list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next

        result.next = list1 or list2
        
        return dummy.next
          
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = dummy = ListNode(-1001, None)

        for head in lists:
            self.merge2Lists(result, head)

        return dummy.next
