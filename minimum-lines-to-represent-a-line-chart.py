import numpy as np

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        data = np.array(stockPrices, dtype=np.int32)
        data = data[data[:,0].argsort()]
        data[:-1] -= data[1:]
        np.floor_divide(data, np.gcd(data[:,0:1], data[:,1:2]), out=data)
        return data.shape[0] - np.count_nonzero(np.all(data[:-2] == data[1:-1], axis=1)) - 1
