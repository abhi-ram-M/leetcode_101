class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n =  len(prices)
        min_price = float('inf')
        max_profit = 0
        for i in prices:
            if min_price > i :
                min_price = i
            max_profit = max(max_profit,i-min_price)
        return max_profit