class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        minOps = k
        count = 0

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                count += 1
            if (r - l + 1) == k:
                minOps = min(count, minOps)
            if (r - l + 1) > k:
                if blocks[l] == 'W':
                    count -= 1
                l += 1
                minOps = min(count, minOps)

        return minOps