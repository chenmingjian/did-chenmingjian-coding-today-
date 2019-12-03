import numpy as np 
import time

begin = time.time()
a = [i for i in range(300000, 0, -1)]

print(a[:10])
a = np.sort(a)
print(a[:10])

print(time.time() - begin)