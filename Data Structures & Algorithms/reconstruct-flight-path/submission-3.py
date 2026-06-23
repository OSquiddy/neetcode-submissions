class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {i: [] for i,_ in tickets }

        for i, j in tickets:
            adj[i].append(j)

        for i in adj.keys():
            adj[i].sort()

        print(adj)

        path = ['JFK']

        def dfs(src):
            if len(path) == len(tickets) + 1:
                return True
            
            if src not in adj:
                return False
            
            temp = list(adj[src])
            for i,v in enumerate(temp):
                adj[src].pop(i)
                path.append(v)
                if dfs(v):
                    return True
                adj[src].insert(i, v)
                path.pop()
            return False
        
        dfs("JFK")
            
        return path