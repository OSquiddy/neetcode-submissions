class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        for idx, num in enumerate(nums):
            complement = target - num
            if complementMap.get(complement) != None:
                return [min(idx, complementMap.get(complement)), max(idx, complementMap.get(complement))]
            else:
                complementMap[num] = idx