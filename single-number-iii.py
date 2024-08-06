import numpy as np
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 2:
            return nums
        x = np.array(nums, dtype=np.int32)
        x.sort()
        if x[-1] != x[-2]:
            vals = [x[-1]]
        else:
            vals = []
        
        true_pos = np.where(x[:-1:2] != x[1::2])[0]

        if vals == []:
            # true_pos is an array of consecutive integers, start and endpoint give the location of anomalies
            return x[[true_pos[0]*2, true_pos[-1]*2+1]].tolist()
        else:
            # only first element is needed
            return [x[true_pos[0] * 2]] + vals
