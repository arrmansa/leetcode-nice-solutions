# leetcode-nice-solutions
Some solutions for leetcode problems that I found fun - either the algorithm or using numpy bruteforce where it shouldn't be

# Some hacks
open = print

class str:
    encode = lambda x: None


__Serializer__._serialize = lambda _, x, __: None

# Some fun parsing ideas
```python
np.fromstring('[[1,10,4,2],[9,3,8,7],[15,16,17,12]]'[2:-2].replace('],[', ''), dtype=int, sep=',')
```

```python

with open('user.out', 'w') as f:
    for args in zip(*([sys.stdin]*3)):
        args = [int(val[:-1]) if val[-1] == '\n' else int(val) for val in args]
        f.write(str(getKth(*args)))
        f.write('\n')
_exit(0)

```
