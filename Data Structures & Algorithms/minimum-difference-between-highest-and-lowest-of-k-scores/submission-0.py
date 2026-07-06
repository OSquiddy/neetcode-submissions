class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        print(nums)
        l = 0
        diff = nums[k-1] - nums[l]
        for r in range(k, len(nums)):
            l += 1
            diff = min(diff, nums[r] - nums[l])
        return diff


        
