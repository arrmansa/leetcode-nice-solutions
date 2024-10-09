def spiraloffset(n, spiral_idx):
    # return n ** 2 - (n - 2 * spiral_idx) ** 2
    return 4 * spiral_idx * (n - spiral_idx)

def spiralposition(i, j, n):
    # Enter
    if i == 0:
        return j
    # Corner 1
    if j == n-1:
        return n - 1 + i
    # Corner 2
    if i == n-1:
        return 3 * n - 3 - j
    # Corner 3
    if j == 0:
        return 4 * n - 4 - i

    raise NotImplementedError((i, j, n))

def getnum(i, j, n):
    spiral_idx = min(i, n-1-i, j, n-1-j)
    return spiraloffset(n, spiral_idx) + spiralposition(i-spiral_idx, j-spiral_idx, n-spiral_idx*2) + 1

def getrow(i, n):
    return (getnum(i, j, n) for j in range(n))

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        return (getrow(i, n) for i in range(n))
