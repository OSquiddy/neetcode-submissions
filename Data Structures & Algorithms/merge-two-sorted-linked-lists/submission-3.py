# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = newHead = ListNode(0)
        
        while list1 and list2:
            if list1.val <= list2.val:
                newHead.next = list1
                list1 = list1.next

            else:
                newHead.next = list2
                list2 = list2.next
        
            newHead = newHead.next
        
        if not list1:
            newHead.next = list2
        
        if not list2:
            newHead.next = list1
        
        return dummy.next
            
