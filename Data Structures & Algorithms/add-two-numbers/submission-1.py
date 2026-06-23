# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        cur = l1
        num1, num2 = 0, 0
        while cur:
            num1 += cur.val * (10 ** count)
            count += 1
            cur = cur.next
        
        count = 0
        cur = l2
        while cur:
            num2 += cur.val * 10 ** count
            count += 1
            cur = cur.next

        result = num1 + num2
        print(result)
        if result == 0:
            return ListNode(0)
        dummy = ListNode(0)
        head = dummy        

        while result > 0:
            newVal = result % 10
            head.next = ListNode(newVal)
            head = head.next
            result = result // 10
        
        return dummy.next