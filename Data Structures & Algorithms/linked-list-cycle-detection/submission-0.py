# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodeMap = set()
        while (head != None):
            if head in nodeMap:
                return True
            else:
                nodeMap.add(head)
                head = head.next
        return False