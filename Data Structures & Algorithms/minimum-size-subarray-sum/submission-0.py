class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minLength = len(nums)

        for r in range(len(nums)):
            total += nums[r]
            while target - total <= 0:
                minLength = min(r - l + 1, minLength)
                total -= nums[l]
                l += 1
            if l == 0 and r == len(nums) - 1:
                return 0

        return minLength