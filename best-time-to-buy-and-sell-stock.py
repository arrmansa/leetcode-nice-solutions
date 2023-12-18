import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)-2, 0, -1):
            if prices[i+1]<=prices[i]<=prices[i-1] or prices[i+1]>=prices[i]>=prices[i-1]:
                del prices[i]
        val = 0
        prices = np.array(prices)
        for i in range(1, len(prices)):
            val = max(val, np.max(prices[i:]) - np.min(prices[:i]))
        return val
