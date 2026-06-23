class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0

        substring = ""
        max_length = 0

        if not s:
            return max_length
        
        # if len(s) == 1:
        #     return len(s)

        # substring += s[i]
        # max_length = 1

        while j < len(s):
            if s[j] not in substring:
                substring += s[j]
                length = len(substring)
                if max_length < length:
                    max_length = length
            else:
                i += 1
                j = i
                substring = s[j]
            j += 1

        return max_length

