class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [1] * len(nums), [1] * len(nums)

        prod = 1
        for i in range(1, len(nums)):
            prod *= nums[i-1]
            prefix[i] = prod
        
        prod = 1
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i+1]
            postfix[i] = prod

        combined = [postfix[i] * prefix[i] for i in range(len(nums))]
        return combined