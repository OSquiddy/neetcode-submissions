class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        max_count = 0

        q = deque([])
        fresh = []

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                if grid[r][c] == 1:
                    fresh.append((r,c))

        while q:
            r, c, time = q.popleft()
            print("current: ", r, c)
            for dr, dc in directions:
                if (
                    0 <= r + dr < rows
                    and 0 <= c + dc < cols
                    and grid[r + dr][c + dc] == 1
                ):
                    print('Exploring', r + dr,c + dc)
                    grid[r + dr][c + dc] = 2
                    q.append((r + dr, c + dc, time + 1))
                    max_count = max(max_count, time + 1)
        
        for r,c in fresh:
            if grid[r][c] == 1:
                return -1
        
        return max_count
