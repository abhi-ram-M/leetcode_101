class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =  len(prices)
        if (1 <= n <= 10**5):
            min_price = float('inf')
            max_profit = 0
            for i in prices:
                min_price = min(min_price,i)
                max_profit = max(max_profit,i-min_price)
            return max_profit