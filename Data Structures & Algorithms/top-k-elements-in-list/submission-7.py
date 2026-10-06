class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}

        for n in nums:
            map[n] = map.get(n, 0) + 1
        
        res = []
        heap = [(v, k) for k,v in map.items()]
        # print(heap)
        while k > 0:
            heapq.heapify_max(heap)
            # _, val = heapq.heappop(heap)
            # print(val)
            res.append(heapq.heappop(heap)[1])
            k -= 1

        return res