# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.getDepth(root.left)
        right = self.getDepth(root.right)

        if abs(left - right) > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.getDepth(root.left), self.getDepth(root.right))