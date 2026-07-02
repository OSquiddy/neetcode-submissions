class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        q = []
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        for key,val in freq.items():
            q.append((val, key))
        
        heapq.heapify_max(q)

        res = []
        while k > 0:
            res.append(heapq.heappop_max(q)[1])
            k -= 1

        return res