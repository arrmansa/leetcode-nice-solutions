from gc import disable
from os import _exit
from sys import stdin 
import json


def soln(l):
    i, j = 0, 1
    while i < len(l) and j < len(l):
        if l[i] != l[j]:
            l[i+1] = l[j]
            i += 1
        j += 1
    del l[i+1:]
    return json.dumps(l, separators=(',', ':'))

with open('user.out', 'w', 1024) as f:
    disable()
    for i in map(json.loads, sys.stdin):
        f.write(soln(i))
        f.write('\n')

_exit(0)
