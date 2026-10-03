class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF = 2**31 - 1
        q = [(0, k)]
        visited = set()
        
        time = {i+1: INF for i in range(n)}
        graph = {i+1: [] for i in range(n)}

        for ui, vi, ti in times:
            graph[ui].append((vi, ti))
        
        time[k] = 0

        while q:
            cur_time, cur = heapq.heappop(q)

            if cur_time > time[cur]:
                continue

            for dest, ti in graph[cur]:
                new_time = cur_time + ti
                if new_time < time[dest]:
                    time[dest] = new_time
                    heapq.heappush(q, (new_time, dest))
                    # visited.add(dest)
        
        return max(time.values()) if INF not in time.values() else -1 
