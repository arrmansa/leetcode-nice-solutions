import numpy as np
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        arr = np.array([[int(e) for e in l] for l in matrix], dtype = np.bool_)
        val = 0
        for c1 in range(arr.shape[0]):
            not_small = lambda c2: (c2-c1)>val
            for c2 in filter(not_small, range(arr.shape[0], c1, -1)):
                fullrows = np.all(arr[c1:c2], axis=0)
                max_width = max(self.truegroups(fullrows))
                val = max(val, min(max_width, c2-c1))
        return val**2
    
    @staticmethod
    def truegroups(arr):
        count = 0
        for i in arr:
            if i:
                count += 1
            elif count:
                yield count
                count = 0
        yield count
