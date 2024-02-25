from itertools import product
import re
import gc
gc.disable()
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        spacednum = sum(([i, None] for i in num), start = [])[:-1]
        successes = []
        for operators in product(*([["*", "+", "-", ""]] * (len(spacednum)//2))):
            for i, op in zip(range(1, len(spacednum), 2), operators):
                spacednum[i] = op
            expr = "".join(spacednum)
            if re.search(r"([^\d]|^)(0+)(\d)", expr):
                continue
            if eval(expr) == target:
                successes.append(expr)
        return successes
