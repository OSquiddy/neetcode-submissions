class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = "({["
        closing = ")}]"
        mapping = { ')': '(', '}': '{', ']': '['}

        for char in s:
            # print(stack, char)
            if char in opening:
                stack.append(char)
            
            if char in closing:
                if not len(stack):
                    return False
                c = stack.pop()
                if c != mapping[char]:
                    return False

        return not bool(len(stack))