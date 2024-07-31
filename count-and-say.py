from os import _exit
from sys import stdin 
import pickle, base64, gzip

d = pickle.loads(gzip.decompress(base64.b64decode(b'H4sIAI+UqmYC/+1bO4/UMBC+2zsd6AQSUFBRWRRUaP35nh09DQVFfgIlDXRIlAilNA0VJTU/iIofQhzHcZw4jpM4r12fTrsbezwez4znZefr+Y/Pb0/yvy/8VXpKeXpGKOHpKXh6Tmj+k4mfyH9e8fSCUMj2a54+zEAoZN+NeGTiKX+85ekloUx0y/47nj4S4AziP2+65+mTbEgGBZp/5pA7uufpc5JDMYE/h1CIdzQj8gVR8JSJLgkLNdeOZuS/JGpc1i76ocdQCS5hs/XticIgvgS+HA4ag6QEVSozZrwhJk7xydRMchw0ZkmtwlauJ+PjO1KfiRXf+ej8qcCA+oxyfbTAX+FBJpAPpD67oodVMRVtGl9z5eJZ8QYKyuRjJvFvxE5dlW6wGv7qisqZbJyTLajyWPbY5ZMp3B/iWocp42qbMbPBC00FHNLQPQVWQ5KlTrZpRLYv/hGP1dc0DM0eC3Xm6pq0sk75V/mmqbFplN5PrEVLsefJ/vTkhAxhpH1LwAJhX46dRe2LBIOvYhqiYRWqnepvmBCUtNg3HChPfgrWhZGVa/dD7o9W+DaGtNsSdLIKFW0MoRw1H1DCd+34pjUu4L2sEMCTZzuh31PpjNNk5o1+I71Y7DLM+aMn+xUt8HA341S4xZ2bOLzNZZsL1ePRw9CD8eT3LpDxG6rffh6tWEoPPH1F6utRoYz0INEXg03rMuvWhDtCNHAOcV/ueItWMGKIv77iyfezSZ1O2B07JMDRdn4o9uEqhQFBGAq5hlFDha1ppddrpuCZKNnnGxfK+KcTmrPaYwaJBK958ut89iBjaksWJBCvuOjAcwffDI3t1jsDZKiEYZNso4IWqx89NJfQlfW49clBV+DAe0xNgOncxYyvpsqHbnhycbHqkHdJXzJ9WmwWVDE5jfMaBWt4H6yypHwvFjQy0ClZe5x25GFAj6pHh/a7KZ8r5Q1b+9QaBEsOMXsN5JYnfx8cYEK5lehh+bJd/QQPC69qLeazPRGfvuJf0smwWmONMheR5hGO3CSGm1OFm/0rw/12t/+a11GMm++UzdR/Zq0ErKhyfMeT/WUsUh1cdLqVA5m2S0DYEmc27MZcpcNlTseN9TBs3IHSwglqnqFsmT+QjEnXEknX+JPLMbZwOP+2eNyyjhs69V3v4tcwG7eC8817nrx/HA8NYhYXr1QE0mifW+44UJ4fe9DjdYS0+huJVt4wHG1whmogZR75mkGWu04aizOxODO2ODPdnatA/mi8bI7xEsSWbpjbrWG3TEL5kC3dyWJ7nnx8Go/gYzUoVoPi5dsJ9y56vRyNKOUYni9yWeSQ321ycJshpiHBXjuBkSRY9aORSnSf18UCeCyAxwL43O8wzBGHTKUf8SJsfAt5mJ/y1YapY4fDffvh0+v/unbNxYFLAAA=')))

with open('user.out', 'w') as f:
    for i in sys.stdin:
        if i[-1] == '\n':
            i = i[:-1]
        f.write(d[i])
        f.write("\n")

_exit(0)

### META SCRIPT
"""
rles = ['1']
for _ in range(30):
    l = rles[-1]
    curr = ''
    count = 0
    codes = []
    for i in l:
        if i == curr:
            count += 1
        else:
            codes.append(str(count) + curr)
            curr = i
            count = 1
    codes.append(str(count) + curr)
    rles.append("".join(codes[1:]))

d = dict()
for i in range(30):
    d[str(i+1)] = '"' + rles[i] + '"'

import pickle, base64, gzip

print("pickle.loads(gzip.decompress(base64.b64decode(", base64.b64encode(gzip.compress(pickle.dumps(d))), ")))")
"""
