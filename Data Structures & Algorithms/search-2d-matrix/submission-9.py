class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowIndexes = [(x[0], x[-1]) for x in matrix]
        targetRow = None
        rowL, rowH = 0, len(rowIndexes) - 1

        # print(rowIndexes, rowL, rowH)

        while rowL <= rowH:
            rowMid = rowL + (rowH - rowL) // 2

            print(target, rowIndexes[rowMid])

            # If the target is the first element of the row
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

            # # If first elem of row is less than target
            # elif rowIndexes[rowMid] < target:
            #     # If there is a next row:
            #     if (rowMid + 1) < len(rowIndexes):
            #         # If first elem of next row is smaller than target, update the left pointer of binary search
            #         if rowIndexes[rowMid + 1] < target:
            #             rowL = rowMid + 1
            #         # If first elem of next row is larger than target, target might exist inside this row
            #         elif rowIndexes[rowMid + 1] > target:
            #             targetRow = matrix[rowMid]
            #             break
            #     else:
            #         targetRow = matrix[rowMid]
            #         break
            
            # # If first elem of row is greater than target:
            # elif rowIndexes[rowMid] > target:
            #     # If first elem of prev row is greater than target, update the right pointer of binary search
            #     if rowIndexes[rowMid - 1] > target:
            #         rowH = rowMid - 1
            #     # If first elem of prev row is smaller than target, target might exist inside the prev row
            #     elif rowIndexes[rowMid - 1] < target:
            #         targetRow = matrix[rowMid - 1]
            #         break
        
        print('Target Row', targetRow)

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