class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        # print(res)
        for s in strs:
            # print()
            # print(s)
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # print(tuple(count))
            res[tuple(count)].append(s)
        return list(res.values())
