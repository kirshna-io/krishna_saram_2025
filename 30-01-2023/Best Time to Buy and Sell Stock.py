class Solution(object):
    def maxProfit(self, prices):

        buy = prices[0]
        max_profit = 0

        for sell in prices:
            if buy > sell:
                buy = sell
            profit = sell - buy
            if profit > max_profit:
                max_profit = profit

        return max_profit
