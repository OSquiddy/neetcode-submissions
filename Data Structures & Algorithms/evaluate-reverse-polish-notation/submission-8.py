class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        first, second = 0, 0
        res = 0
        stack = []

        for char in tokens:
            if char not in "+-*/":
                stack.append(int(char))
            else:
                # print(char)
                first, second = stack.pop(), stack.pop()
                if char == "+":
                    res = first + second
                elif char == "-":
                    res = second - first
                elif char == "*":
                    res = first * second
                elif char == "/":
                    res = int(second / first)
                stack.append(res)
            # print(res, stack)

        return stack[0]