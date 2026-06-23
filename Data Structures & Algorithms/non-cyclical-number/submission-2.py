class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def getSquareOfDigits(n):
            ans = 0
            while n:

                remainder = n % 10
                ans += remainder ** 2
                n //= 10
            return ans

        while True:
            square = getSquareOfDigits(n)
            if square == 1:
                return True
            if square in visit:
                return False
            visit.add(square)
            n = square