class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
            if hashmap[num] > 1:
                return True
        
        return False