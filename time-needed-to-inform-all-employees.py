from functools import cache
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        @cache
        def get_needed_time(x):
            return get_needed_time(manager[x]) + informTime[x] if x != -1 else 0
        return max(map(get_needed_time, range(n)))
