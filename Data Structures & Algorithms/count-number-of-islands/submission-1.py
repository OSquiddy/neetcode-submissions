class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Set up variables
        numIslands = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # Keep track of visited nodes or change visited nodes to 0
        # Use DFS
        def dfs(r, c):
            grid[r][c] = "0"

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] == '0'):
                    continue
                dfs(nr, nc)
        
        # Count number of islands
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    numIslands += 1

        return numIslands