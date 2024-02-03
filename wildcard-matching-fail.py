# An interesting problem. It feels like just using regex should get all testcases, but apperently not? this solution requires an implementation that is faster than regex. Pretty interesting. This passes 1710 / 1811 testcases.
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        l = len(s) - len(p.replace('?', '').replace('*', ''))
        new_pattern = re.sub(r"\*+", f".{{0,{l}}}", p).replace('?', '.')
        return re.fullmatch('^' + new_pattern + '$', s)
