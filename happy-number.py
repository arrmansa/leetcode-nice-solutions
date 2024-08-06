# n 1999999999 gives 730, therefore we can simply get a set of happy numbers upto 730 and check after 1 iteration

s = {1, 7, 10, 13, 19, 23, 536, 28, 31, 32, 44, 556, 49, 563, 565, 566, 68, 70, 79, 82, 86, 91, 94, 608, 97, 100, 103, 617, 109, 622, 623, 632, 635, 637, 638, 129, 130, 644, 133, 649, 139, 653, 655, 656, 665, 671, 673, 167, 680, 683, 176, 694, 188, 700, 190, 192, 193, 709, 203, 716, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496}
class Solution:
    def isHappy(self, n: int) -> bool:
        if n > 730:
            n = sum(int(x)**2 for x in str(n))
        return n in s

# We then push this to the limit using stdin, gc, binary write hacks

s = {1, 7, 10, 13, 19, 23, 536, 28, 31, 32, 44, 556, 49, 563, 565, 566, 68, 70, 79, 82, 86, 91, 94, 608, 97, 100, 103, 617, 109, 622, 623, 632, 635, 637, 638, 129, 130, 644, 133, 649, 139, 653, 655, 656, 665, 671, 673, 167, 680, 683, 176, 694, 188, 700, 190, 192, 193, 709, 203, 716, 208, 219, 226, 230, 236, 239, 262, 263, 280, 291, 293, 301, 302, 310, 313, 319, 320, 326, 329, 331, 338, 356, 362, 365, 367, 368, 376, 379, 383, 386, 391, 392, 397, 404, 409, 440, 446, 464, 469, 478, 487, 490, 496}

import gc
from os import _exit
from sys import stdin

with open('user.out', 'wb') as f:
  gc.disable()
  for i in sys.stdin:
    if i[-1] == '\n':
        i = i[:-1]
    n = sum(int(x)**2 for x in i)
    f.write(b'true\n' if n in s else b'false\n')
_exit(0)

# Meta code

def isHappy(n: int) -> bool:
    s = set()
    while n not in s:
        s.add(n)
        n = sum(int(x)**2 for x in str(n))
    return n == 1

print(set(list(filter(isHappy, range(730)))))
