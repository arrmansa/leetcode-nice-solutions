from scipy.ndimage import _ni_label, label
import numpy as np
old = _ni_label.get_write_line
empty = np.empty(0)
mockval = old(empty)
_ni_label.get_write_line = lambda _: mockval

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = np.array(grid, dtype=np.uint8)
        return label(grid, output=grid)
