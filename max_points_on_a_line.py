import numpy as np
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        """"
        a brute force with np.dstack and np.unique that works surprisingly well on https://leetcode.com/problems/max-points-on-a-line
        """"
        if len(points) == 1:
            return 1
        points = np.array(points)
        # Set constants for equation ax - by = c
        deltax = points[:, 0] - points[:, 0, np.newaxis]
        deltay = points[:, 1] - points[:, 1, np.newaxis]
        const = points[:, 1] * deltax - points[:, 0] * deltay
        # Calculate unique (a/c, b/c) pairs where c != 0
        data = np.dstack((deltax/const, deltay/const))[const != 0]
        if len(data):
            count = max(np.unique(data, axis=0, return_counts=True)[1])
            normal = int(count**0.5) + 1  # reverses x**2 - x easily
        else:
            normal = 0
        # Calculate unique (a/b when c = 0 and b != 0)
        data = (deltax/deltay)[np.logical_and(deltay != 0,  const==0)]
        if len(data):
            count = max(np.unique(data, axis=0, return_counts=True)[1])
            through_origin = int(count**0.5) + 1  # reverses x**2 - x easily
        else:
            through_origin = 0
        # b == 0 and c == 0 implies y axis (a simple check works here)
        y_axis = np.sum(points[:, 1] == 0)
        return max(through_origin, normal, y_axis)
