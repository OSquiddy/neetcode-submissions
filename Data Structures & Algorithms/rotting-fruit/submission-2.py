class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque()

        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c, time))
        
        while fresh >= 0 and q:
            row, col, time = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc

                if (nr < 0 or nc < 0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != 1):
                    continue
                
                if grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc, time + 1))
                    fresh -= 1
                    

        
        return time if fresh <= 0 else -1
