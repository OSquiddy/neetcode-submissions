class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for char in s:
            if chars.get(char):
                chars[char] += 1
            else:
                chars[char] = 1

        for char in t:
            if chars.get(char):
                chars[char] -= 1
            else:
                return False
        
        for key, value in chars.items():
            if value > 0:
                return False

        return True