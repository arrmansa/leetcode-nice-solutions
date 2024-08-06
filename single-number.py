import numpy as np
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        x = np.array(nums, dtype=np.int16)
        x.sort()
        if x[-1] != x[-2]:
            return x[-1]
        true_pos = (x[:-1:2] != x[1::2]).argmax()
        return int(x[true_pos * 2])
