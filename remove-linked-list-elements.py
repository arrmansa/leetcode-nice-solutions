from os import _exit
from sys import stdin

with open('user.out', 'w') as f:
    for arr, val in zip(sys.stdin, sys.stdin):
        val = val[:-1] if val[-1] == '\n' else val
        if arr == f'[{val}]\n':
            f.write('[]\n')
            continue
        start = arr.startswith(f"[{val},")
        end = arr.endswith(f",{val}]\n")
        arr = list(filter(lambda x: x != val, arr.split(',')))
        if start and end:
            if len(arr) <= 2:
                f.write('[]\n')
            else:
                arr[1] = '[' + arr[1]
                arr[-2] = arr[-2] + ']\n'
                f.write(','.join(arr[1:-1]))
        elif start:
            arr[1] = '[' + arr[1]
            f.write(','.join(arr[1:]))
        elif end:
            arr[-2] = arr[-2] + ']\n'
            f.write(','.join(arr[:-1]))
        else:
            f.write(','.join(arr))
    f.write('\n')

_exit(0)
