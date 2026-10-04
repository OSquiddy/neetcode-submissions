class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles = sorted(piles)
        min_k = piles[-1]
        l, r = 1, piles[-1] + 1

        while l <= r:
            k = l + (r - l) // 2
            time = 0
            for bananas in piles:
                time += bananas//k if bananas % k == 0 else (bananas//k) + 1

            if time > h:
                l = k + 1
            
            if time <= h:
                r = k - 1
                min_k = min(min_k, k)


        return min_k