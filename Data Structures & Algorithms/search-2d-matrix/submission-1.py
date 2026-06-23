class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lower = 0
        upper = len(matrix) - 1

        while (lower <= upper):

            mid = lower + ((upper - lower) // 2)

            if target < matrix[mid][0]:
                upper = mid - 1
            elif target > matrix[mid][(len(matrix[mid]) - 1)]:
                lower = mid + 1
            else:
                break

        if not (lower <= upper):
            return False

        mid = lower + (upper - lower) // 2
        left = 0
        right = len(matrix[mid]) - 1

        while (left <= right):

            innerMid = left + ((right - left) // 2)

            if target < matrix[mid][innerMid]:
                right = innerMid - 1
            elif target > matrix[mid][innerMid]:
                left = innerMid + 1
            elif target == matrix[mid][innerMid]:
                return True
        
        return False