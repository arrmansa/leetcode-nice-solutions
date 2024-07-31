# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from gc import disable
disable()
from os import _exit
from sys import stdin 
import json

data = list(map(json.loads, sys.stdin))

def soln(l, n):
    del l[len(l)-n]
    return json.dumps(l, separators=(',', ':'))

outs = []
for args in (data[i:i+2] for i in range(0, len(data), 2)):
    outs.append(soln(*args))

outs.append("")

with open('user.out', 'w') as f:
    f.write("\n".join(outs))

_exit(0)
