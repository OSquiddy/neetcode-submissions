# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        q = deque()
        q.append(root)

        cache = []

        while q:
            node = q.popleft()
            
            heapq.heappush_max(cache, node.val)

            if len(cache) > k:
                heapq.heappop_max(cache)
            
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        

        return heapq.heappop_max(cache)