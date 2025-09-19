class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if not (1 <= n <= 10**5):
            return 0
        for p in prices:
            if not (0 <= p <= 10**4):
                return 0
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit
