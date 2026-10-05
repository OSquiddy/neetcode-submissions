# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node, depth):
            if not node:
                return depth
            
            return max(dfs(node.left, depth + 1), dfs(node.right, depth + 1))
        
        def postOrderTraversal(node, depth, diameter):
            if not node:
                return 0

            # postOrderTraversal(node.left, depth, diameter)
            # postOrderTraversal(node.right, depth, diameter)
            leftMax = dfs(node.left, depth)
            rightMax = dfs(node.right, depth)

            res = (leftMax + rightMax)
            print(node.val, res, leftMax, rightMax)
            diameter = max(res, diameter)

            LDia = postOrderTraversal(node.left, depth, 0)
            RDia = postOrderTraversal(node.right, depth, 0)

            return max(diameter, LDia, RDia)

        return postOrderTraversal(root, 0, diameter)

        # return diameter