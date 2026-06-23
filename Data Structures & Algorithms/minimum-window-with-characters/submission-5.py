class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": 
            return ""

        tMap, window = {}, {}

        for char in t:
            tMap[char] = 1 + tMap.get(char, 0)

        matches, need = 0, len(tMap)
        minSubstringIdx, minLen = [-1, -1], float("infinity")
        l = 0
        for r, char in enumerate(s):
            window[char] = 1 + window.get(char, 0)

            if char in tMap and window[char] == tMap[char]:
                matches += 1

            while matches == need:
                # update our result
                if (r - l + 1) < minLen:
                    minSubstringIdx = [l, r]
                    minLen = (r - l + 1)
                # pop from left of our window
                window[s[l]] -= 1
                if s[l] in tMap and window[s[l]] < tMap[s[l]]:
                    matches -= 1
                l += 1

        l, r = minSubstringIdx
        return s[l:r+1] if minLen != float("infinity") else ""
                

