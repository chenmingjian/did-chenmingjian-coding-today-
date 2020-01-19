from typing import *
import numpy as np
import time
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        mat = np.array(mat)
        m, n = mat.shape
        print(mat)
        max_ = 0
        for i in range(m):
            if i+max_ > m:
                continue
            for j in range(n):
                if j+max_ > n:
                    continue
                sub_mat = mat[i:i+max_, j:j+max_]
                sum_ = np.sum(sub_mat)
                while sum_ <= threshold:
                    print(sub_mat, i, i+max_, j, j+max_)
                    max_ += 1
                    sub_mat = mat[i:i+max_, j:j+max_]
                    sum_ = np.sum(sub_mat)
                    if j+max_ > n or i+max_ > m:
                        break
        return max_ - 1 


start = time.time()
# tmp = Solution().maxSideLength([[28,39,98,91,7,99],[79,3,17,83,9,92],[81,73,42,27,67,70],[88,30,73,99,96,89],[27,59,0,1,65,79],[42,55,48,29,86,96]], 24829)
tmp = Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)
print(tmp)
print(time.time()-start)