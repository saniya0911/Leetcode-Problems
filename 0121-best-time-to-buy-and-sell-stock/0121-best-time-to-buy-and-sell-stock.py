class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        maxprofit = 0
        currprofit = 0
        buy = 0
        n = len(prices)
        for i in range(1, n):
            if prices[i] < prices[buy]:
                buy = i
                maxprofit = max(maxprofit, currprofit)
                currprofit = 0
            elif prices[i] > prices[buy]:
                currprofit = prices[i] - prices[buy]
                maxprofit = max(maxprofit, currprofit)
        return max(maxprofit, currprofit)
