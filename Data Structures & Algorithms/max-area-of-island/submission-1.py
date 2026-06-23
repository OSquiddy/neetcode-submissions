class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        max_count = 0

        def dfs(i, j):

            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            area = 1

            for dr, dc in directions:
                area += dfs(i + dr, j + dc)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_count = max(max_count, dfs(r, c))
        
        return max_count