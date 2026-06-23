class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l, r = 0, len(heights) - 1
        while l < r:
            length = r - l
            breadth = min(heights[l], heights[r])
            area = length * breadth
            if area > result:
                result = area
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return result