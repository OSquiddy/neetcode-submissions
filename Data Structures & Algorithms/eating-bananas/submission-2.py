class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)

        min_k = upper

        while lower <= upper:

            k = lower + (upper - lower) // 2

            count = 0
            for pile in piles:
                count += math.ceil(float(pile) / k)
            if count <= h:
                min_k = k
                upper = k - 1
            else:
                lower = k + 1
        return min_k