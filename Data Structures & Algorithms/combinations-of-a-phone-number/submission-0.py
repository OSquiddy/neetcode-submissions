class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        perm = ""

        def dfs(i):
            nonlocal perm
            if len(perm) == len(digits) and perm:
                res.append(perm)

            if i >= len(digits):
                return

            for char in charMap[digits[i]]:
                perm += char
                dfs(i+1)
                perm = perm[:-1]
        
        dfs(0)
        return res
