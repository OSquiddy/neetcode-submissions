class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_elem = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = l + (r - l) // 2
            min_elem = min(min_elem, nums[mid])
            
            if nums[l] < nums[r]:
                min_elem = min(min_elem, nums[l])
                break
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return min_elem