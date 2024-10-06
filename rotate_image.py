# It's a fun solution, because you take each coordinate in the top quadrant, and then apply a rotation function for that cell instead of reverse etc. Also short and intuitive.
def make_swaps(matrix, i, j, n):
    v = matrix[i][j]
    for _ in range(4):
        i, j = j, n-1-i
        v, matrix[i][j] = matrix[i][j], v

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n//2):
            for j in range(i, n-1-i):
                make_swaps(matrix, i, j, n)
