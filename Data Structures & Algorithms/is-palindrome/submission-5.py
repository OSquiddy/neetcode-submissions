import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = re.sub("[^A-Za-z0-9]+", "", s).lower()
        j = len(cleaned) - 1
        for i in range(len(cleaned) // 2):
            if cleaned[i] == cleaned[j]:
                j -= 1
            else:
                return False
        return True