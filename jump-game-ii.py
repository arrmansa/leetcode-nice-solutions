# A very interesting hack with cache, iter and range, where the iterator is exausted on first run

import itertools
from functools import cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        positions = set([0])

        @cache
        def get_range(i):
            return iter(range(i+1, i+nums[i]+1))

        while len(nums)-1 not in positions:
            positions = set(itertools.chain.from_iterable(map(get_range, positions)))
            jumps += 1
        return jumps
