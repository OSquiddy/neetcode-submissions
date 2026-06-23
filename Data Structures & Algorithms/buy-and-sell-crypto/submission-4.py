class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        if not prices or len(prices) == 1:
            return max_profit

        print(prices)
        
        first = 0
        second = 1
        print(prices[second])

        while second < len(prices):
            if prices[first] > prices[second]:
                first = second
            else:
                print(first, second, profit, max_profit)
                if second >= len(prices):
                    break
                profit = prices[second] - prices[first]
                if profit > max_profit:
                    max_profit = profit
            second += 1
        return max_profit