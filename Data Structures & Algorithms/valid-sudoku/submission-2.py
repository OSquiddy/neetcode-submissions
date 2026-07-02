class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print('Started')
        
        # Rows
        for row in board:
            if not self.isValidRow(row):
                # continue
                return False
        # Cols
        for i in range(len(board)):
            col = []
            for j in range(len(board[0])):
                col.append(board[j][i])
            if not self.isValidCol(col):
                # continue
                return False
        # Grid
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == '.':
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        
        return True

    def isValidRow(self, row):
        freq = {}
        for r in row:
            freq[r] = freq.get(r, 0) + 1
            if r != '.' and freq[r] > 1:
                return False
        return True

    def isValidCol(self, col):
        freq = {}
        for c in col:
            freq[c] = freq.get(c, 0) + 1
            if c != '.' and freq[c] > 1:
                return False
        return True
    
    def isValidGrid(self, grid):
        freq = {}
        for r in range(3):
            for c in range(3):
                freq[(r,c)] = freq.get((r,c), 0) + 1
                if (r,c) != '.' and freq[(r,c)] > 1:
                    return False
        return True