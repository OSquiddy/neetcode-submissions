# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        depth = self.inOrder(root, 0)
        return depth

    def inOrder(self, root, depth):
        depth += 1
        maximum_left, maximum_right = 0, 0
        if root and root.left:
            maximum_left = self.inOrder(root.left, depth)
        if root and root.right:
            maximum_right = self.inOrder(root.right, depth)
        return max(maximum_left, maximum_right, depth)