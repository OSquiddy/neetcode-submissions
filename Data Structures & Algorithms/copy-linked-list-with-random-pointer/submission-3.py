"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        clonedNodes = {None: None}
        cur = head

        while cur and cur not in clonedNodes:
            clone = Node(cur.val)
            clonedNodes[cur] = clone
            # print(cur.val)
            cur = cur.next
            # lastCloned = clone
        
        # print(clonedNodes)

        cur = head
        while cur:
            clonedNodes[cur].next = clonedNodes[cur.next]
            clonedNodes[cur].random = clonedNodes[cur.random]
            cur = cur.next
        
        return clonedNodes[head]
