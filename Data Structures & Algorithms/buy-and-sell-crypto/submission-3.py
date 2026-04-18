class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        start = prices[0]
        for i in range(0, len(prices)):
            dif = prices[i]-start
            maximum = max(dif,maximum)
            start = min(start,prices[i])
        return maximum