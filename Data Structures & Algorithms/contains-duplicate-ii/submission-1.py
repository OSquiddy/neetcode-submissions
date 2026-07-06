class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        seenNums = set()
        
        for r, _ in enumerate(nums):
            if abs(l - r) > k:
                seenNums.remove(nums[l])
                l += 1
            if nums[r] in seenNums:
                return True
            elif nums[r] not in seenNums:
                seenNums.add(nums[r])
        
        return False