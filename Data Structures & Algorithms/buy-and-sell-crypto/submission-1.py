class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy = 0
        sell = 1
        while sell < len(prices):
            cur_profit = prices[sell] - prices[buy]
            res = max(res, cur_profit)
            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy + 1 
            else:
                sell += 1
        return res

