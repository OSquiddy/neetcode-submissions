class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1: 
            return 1
        
        if n == 2:
            return 2
        
        prev, prev_prev = 2, 1
        cur = 0
        for i in range(3, n + 1):
            cur = prev + prev_prev
            prev_prev = prev
            prev = cur
        
        return cur