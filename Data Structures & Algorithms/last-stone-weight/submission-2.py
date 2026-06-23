class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        heapq.heapify_max(stones)
        while len(stones) > 1:
            x, y = heapq.heappop_max(stones), heapq.heappop(stones)
            if x > y:
                heapq.heappush_max(stones, x - y)
            elif y > x:
                heapq.heappush_max(stones, y - x)
            heapq.heapify_max(stones)
        if len(stones) == 1:
            return heapq.heappop_max(stones)
        else:
            return 0