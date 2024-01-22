class Solution:
    def reverse(self, x: int) -> int:
        n = int(str(x)[:0 if x < 0 else None:-1]) * (-1 if x < 0 else 1)
        return n if n in range(int(-2**31), int(2**31)-1) else 0
