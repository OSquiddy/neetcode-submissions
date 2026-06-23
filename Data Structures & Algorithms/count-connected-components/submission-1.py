class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = { i: [] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        res = []
        completed = set()

        def dfs(i, prev, visited):
            completed.add(i)
            if i in visited:
                return
            
            visited.add(i)

            for j in adj[i]:
                if j == prev:
                    continue
                dfs(j, i, visited)
            
            return visited
        
        for i in range(n):
            if i not in completed:
                visited = dfs(i, -1, set())
                res.append(visited)
        
        return len(res)

        