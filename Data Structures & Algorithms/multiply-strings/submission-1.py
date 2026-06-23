class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        x, y = 0, 0
        number_map = {
            ord('0'): 0,
            ord('1'): 1,
            ord('2'): 2,
            ord('3'): 3,
            ord('4'): 4,
            ord('5'): 5,
            ord('6'): 6,
            ord('7'): 7,
            ord('8'): 8,
            ord('9'): 9
        }
        char_map = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

        for idx, char in enumerate(reversed(num1)):
            x += number_map[ord(char)] * (10**idx)

        for idx, char in enumerate(reversed(num2)):
            y += number_map[ord(char)] * (10**idx)

        ans = x * y
        s = ""
        while ans:
            digit = ans % 10
            s += char_map[digit]
            ans //= 10

        
        return "".join(reversed(s))

         