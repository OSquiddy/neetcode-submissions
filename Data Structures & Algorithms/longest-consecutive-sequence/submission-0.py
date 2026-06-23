class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        print(nums_set)

        for elem in nums_set:
            if (elem - 1) not in nums_set:
                current = 0
                val = elem
                while (val in nums_set):
                    val += 1
                    current += 1
                if current > longest:
                    longest = current
        
        return longest