class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = x
        if n > 0:
            for i in range(n - 1):
                ans *= x
        elif n < 0:
            for i in range(-1 * n + 1):
                ans /= x
        else:
            ans = 1
        return ans