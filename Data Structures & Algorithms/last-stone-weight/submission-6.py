class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            print(x, y, stones)
            if x < y:
                heapq.heappush_max(stones, y - x)
            else:
                heapq.heappush_max(stones, x - y)
        stones.append(0)
        return stones[0]