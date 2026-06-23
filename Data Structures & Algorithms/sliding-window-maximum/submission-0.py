class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i in range(len(nums) - k + 1):
            subArray = nums[i:i+k]
            maxElem = max(subArray)
            result.append(maxElem)

        return result