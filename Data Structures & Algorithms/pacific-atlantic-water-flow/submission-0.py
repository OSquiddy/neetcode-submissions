class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # get heights dimensions
        rows, cols = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        pac, atl = set(), set()

        def dfs(i, j, visit, prevHeight):
            if ((i, j) in visit or
                i < 0 or j < 0 or
                i == rows or j == cols or
                heights[i][j] < prevHeight
            ):
                return

            visit.add((i, j))
            
            for dr, dc in directions:
                dfs(i + dr, j + dc, visit, heights[i][j])
            
        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pac and (r,c) in atl:
                    res.append([r, c])
        return res