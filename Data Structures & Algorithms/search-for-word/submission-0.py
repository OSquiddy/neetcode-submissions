class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        answer = None
        
        def findStartingPoints(board, char):
            starting_points = []
            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    if val == char:
                        starting_points.append([i, j])
            return starting_points

        def dfs(gridPts, candidate, word):
            nonlocal answer
            x, y = gridPts[0], gridPts[1]
            print(candidate, word, candidate == word)

            if candidate == word:
                answer = candidate
                return True

            allVisited = True
            for entry in visited.values():
                if entry == 0:
                    allVisited = False
            if allVisited:
                return

            if len(candidate) > len(word):
                return

            # Explore top:
            if x > 0 and visited[(x-1, y)] == 0:
                candidate += board[x-1][y]
                visited[(x-1, y)] = 1
                print("Exploring Top:", candidate)
                dfs((x - 1, y), candidate, word)
                candidate = candidate[:-1]
                visited[(x-1, y)] = 0
            
            # Explore right:
            if y < len(board[0]) - 1 and visited[(x, y+1)] == 0:
                candidate += board[x][y + 1]
                visited[(x, y+1)] = 1
                print("Exploring Right:", candidate)
                dfs((x, y+1), candidate, word)
                candidate = candidate[:-1]
                visited[(x, y+1)] = 0
            
            # Explore down:
            if x < len(board) - 1 and visited[(x+1, y)] == 0:
                candidate += board[x+1][y]
                visited[(x+1, y)] = 1
                print("Exploring Down:", candidate)
                dfs((x+1, y), candidate, word)
                candidate = candidate[:-1]
                visited[(x+1, y)] = 0

            # Explore left
            if y > 0 and visited[(x, y - 1)] == 0:
                candidate += board[x][y-1]
                visited[(x, y-1)] = 1
                print("Exploring Left:", candidate)
                dfs((x, y-1), candidate, word)
                candidate = candidate[:-1]
                visited[(x, y-1)] = 0
                

        
        if not board or not word:
            return False

        startingPoints = findStartingPoints(board, word[0])

        for pts in startingPoints:
            print("\nStarting Points:", pts)
            visited = {}
            candidate = ""

            for i, row in enumerate(board):
                for j, val in enumerate(row):
                    if i == pts[0] and j == pts[1]:
                        visited[(i, j)] = 1
                    else:
                        visited[(i, j)] = 0

            dfs(pts, word[0], word)

            print(answer)

            if answer:
                print("Result is being returned")
                return True

        return False