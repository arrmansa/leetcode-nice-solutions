import numpy as np
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        for i in range(len(prices)-2, 0, -1):
            if prices[i+1]<=prices[i]<=prices[i-1] or prices[i+1]>=prices[i]>=prices[i-1]:
                del prices[i]
        if len(prices) < 2:
            return 0
        prices = np.array(prices, dtype=np.int32)
        loc = np.arange(prices.shape[0], dtype=np.int32)
        pdiff = prices[:,np.newaxis] - prices[np.newaxis, :]
        future = loc[:,np.newaxis] > loc[np.newaxis, :]
        best = np.max(pdiff[future])
        return max(best, 0)
