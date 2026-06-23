class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        def getSquareOfDigits(n):
            ans = 0
            print('Number: ', n)
            while n:

                remainder = n % 10
                print('Current Digit: ', remainder)
                ans += remainder ** 2
                n //= 10
            print('Sum of squares of digits: ', ans)
            return ans

        while True:
            square = getSquareOfDigits(n)
            print(visit, square)
            if square == 1:
                return True
            if square in visit:
                return False
            visit.add(square)
            n = square