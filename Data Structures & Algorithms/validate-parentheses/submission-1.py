class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        complement = { ')': '(', ']': '[', '}': '{' }

        for char in s:
            if char in complement:
                if stack and stack[-1] == complement[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
            
        return True if not stack else False