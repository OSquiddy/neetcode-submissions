# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        
        if not l2:
            return l1
        
        if not (l1 and l2):
            return 0
        
        count1, count2 = 0, 0
        n1, n2 = 0, 0
        
        while l1:
            n1 += 10**count1 * l1.val
            count1 += 1
            l1 = l1.next
        
        while l2:
            n2 += 10**count2 * l2.val
            count2 += 1
            l2 = l2.next
        
        res = n1 + n2
        print(res)

        if res == 0:
            return ListNode(0)


        dummy = cur = ListNode()
        while res > 0:
            cur.next = ListNode(res % 10)
            res //= 10
            cur = cur.next
        
        return dummy.next