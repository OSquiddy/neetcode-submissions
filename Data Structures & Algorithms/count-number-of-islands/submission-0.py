class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(i, j):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
                return False

            grid[i][j] = '0'
        
            dfs(i - 1, j),
            dfs(i + 1, j),
            dfs(i, j + 1),
            dfs(i, j - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r,c)
        
        return island_count



