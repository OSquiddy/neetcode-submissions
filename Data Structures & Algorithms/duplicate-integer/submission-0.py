class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        visited = {}
        for num in nums:
            if visited.get(num):
                return True
            else:
                visited[num] = 1
        return False
         