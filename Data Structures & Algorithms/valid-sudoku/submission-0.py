class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        tiles = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in columns[c] or
                    board[r][c] in tiles[(r//3, c//3)]):
                    return False
                columns[c].add(board[r][c])
                rows[r].add(board[r][c])
                tiles[(r//3, c//3)].add(board[r][c])
        return True