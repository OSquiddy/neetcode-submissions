"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        nodes = {}

        def dfs(current):
            if current in nodes:
                return nodes[current]
            
            copy = Node(current.val)
            nodes[current] = copy

            for n in current.neighbors:
                copy.neighbors.append(dfs(n))
            
            return copy
                    
        return dfs(node) if node else None
            