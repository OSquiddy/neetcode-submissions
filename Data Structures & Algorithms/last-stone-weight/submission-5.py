class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        while len(stones) >= 2:
            heapq.heapify_max(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            print(x, y, stones)

            if x == y:
                continue
            else:
                heapq.heappush(stones, max(y, x) - min(y,x))
            
        return stones[0] if stones else 0