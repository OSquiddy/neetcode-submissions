# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right))
        
        return False
        
    def inOrder(self, root, subRoot):
        if root and subRoot and root.val == subRoot.val:
            if root.left and subRoot.left and root.left == subRoot.left:
                self.inOrder(root.left, subRoot.left)
            if root.right and subRoot.right and root.right == subRoot.right:
                self.inOrder(root.right, subRoot.right)
            return True
        return False