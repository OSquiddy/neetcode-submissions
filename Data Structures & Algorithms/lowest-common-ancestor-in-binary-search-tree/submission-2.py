# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pAnc, qAnc = None, None

        def dfs(node, target, anc, x):
            nonlocal pAnc, qAnc

            if not node:
                return

            if target == node:
                if x == 'p':
                    pAnc = anc
                else:
                    qAnc = anc
            
            if node.left:
                dfs(node.left, target, anc + deque([node.left]), x)
            
            if node.right:
                dfs(node.right, target, anc + deque([node.right]), x)
        
        dfs(root, p, deque([root]), 'p')
        dfs(root, q, deque([root]), 'q')

        intersection = []

        qInd, pInd = 0, 0
        i = 0
        while pAnc and qAnc:
            if pAnc[0] == qAnc[0]:
                intersection.append(pAnc[0])
            else:
                break
            pAnc.popleft()
            qAnc.popleft()

        return intersection[-1]
