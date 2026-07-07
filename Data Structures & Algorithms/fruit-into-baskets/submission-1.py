class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = {}
        maxF, l = 0, 0

        for r, _ in enumerate(fruits):
            baskets[fruits[r]] = 1 + baskets.get(fruits[r], 0)

            while len(baskets) > 2:
                baskets[fruits[l]] -= 1
                if baskets[fruits[l]] == 0:
                    baskets.pop(fruits[l])
                l += 1
            
            maxF = max(maxF, sum([x for x in baskets.values()]))

        return maxF
                        