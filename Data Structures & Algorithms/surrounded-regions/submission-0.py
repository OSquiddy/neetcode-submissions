class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # find connected group of Os surrounded by Xs
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        visited = set()

        border_pts = []

        for r in range(rows):
            for c in range(cols):
                if r == 0 or c == 0 or r == rows - 1 or c == cols - 1 and board[r][c] == 'O':
                    border_pts.append((r,c))


        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X' or (r,c) in visited):
                return

            visited.add((r,c))
            
            if board[r][c] == 'O':
                board[r][c] = '#'

            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r,c in border_pts:
            dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == '#':
                    board[r][c] = 'O'
