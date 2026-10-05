# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        totalNodes, badNodes = 0, 0

        def dfs(node, anc, prevMax):
            nonlocal totalNodes, badNodes

            if not node:
                return

            prevMax = max(prevMax, node.val)
            if prevMax > node.val:
                badNodes += 1
            
            totalNodes += 1
            
            if node.left:
                dfs(node.left, anc + [node.left.val], prevMax)
            
            if node.right:
                dfs(node.right, anc + [node.right.val], prevMax)
        
        dfs(root, [root.val], root.val)

        return totalNodes - badNodes