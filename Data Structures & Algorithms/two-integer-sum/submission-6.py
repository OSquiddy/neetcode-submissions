class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        charMap = {}
        for idx, num in enumerate(nums):
            charMap[num] = idx

        for idx, num in enumerate(nums):
            if target - num in charMap and idx != charMap.get(target - num):
                return [idx, charMap[target - num]]

        return [] 