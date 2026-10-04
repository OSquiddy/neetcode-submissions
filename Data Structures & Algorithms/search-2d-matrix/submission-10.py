class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIndexes = [(x[0], x[-1]) for x in matrix]
        targetRow = None
        rowL, rowH = 0, len(rowIndexes) - 1

        while rowL <= rowH:
            rowMid = rowL + (rowH - rowL) // 2

            if rowIndexes[rowMid][0] == target or rowIndexes[rowMid][1] == target:
                return True
            
            elif rowIndexes[rowMid][0] < target < rowIndexes[rowMid][1]:
                targetRow = matrix[rowMid]
                break
            
            elif rowIndexes[rowMid][1] < target:
                if rowMid + 1 < len(rowIndexes):
                    rowL = rowMid + 1
                else:
                    return False
            
            elif rowIndexes[rowMid][0] > target:
                if rowMid - 1 < 0:
                    return False
                else:
                    rowH = rowMid - 1
        
        if targetRow:
            l, r = 0, len(targetRow) - 1

            while l <= r:
                mid = l + (r - l) // 2
                print(mid)
                if targetRow[mid] == target:
                    return True
                elif targetRow[mid] < target:
                    l = mid + 1
                elif targetRow[mid] > target:
                    r = mid - 1

        return False