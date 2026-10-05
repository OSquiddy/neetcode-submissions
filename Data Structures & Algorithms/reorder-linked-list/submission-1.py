# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = None
        fast, slow = head, head
        l1_end = None
        
        while fast and fast.next:
            l1_end = slow
            slow = slow.next
            fast = fast.next.next
        
        l2_head = slow.next
        slow.next = None

        prev, cur = None, l2_head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        L1 = head
        reversedL2 = prev

        while reversedL2:
            tmp1, tmp2 = L1.next, reversedL2.next
            L1.next = reversedL2
            reversedL2.next = tmp1
            L1, reversedL2 = tmp1, tmp2