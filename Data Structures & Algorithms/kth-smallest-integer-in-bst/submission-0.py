# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []

        def inOrder(root):
            nonlocal array

            if root and root.left:
                inOrder(root.left)
            
            array.append(root.val)

            if root and root.right:
                inOrder(root.right)

        inOrder(root)

        print(array)

        return array[k - 1]