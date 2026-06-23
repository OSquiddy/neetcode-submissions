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
        newNodes = {None: None}

        node = head
        while node:
            newNodes[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            newNodes[node].next = newNodes[node.next]
            newNodes[node].random = newNodes[node.random]
            node = node.next
        
        return newNodes[head]