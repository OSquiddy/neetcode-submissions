"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
        
        nodes = {}
        nodes[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for nei in cur.neighbors:
                if nei not in nodes:
                    nodes[nei] = Node(nei.val)
                    q.append(nei)
                nodes[cur].neighbors.append(nodes[nei])
        
        return nodes[node]
        
            