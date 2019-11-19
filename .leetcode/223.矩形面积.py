#
# @lc app=leetcode.cn id=223 lang=python3
#
# [223] 矩形面积
#
from typing import *
# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        a = [A, C, E, G]
        a.sort()
        b = [D, H, B, F]
        b.sort()

        w0 = C-A
        w1 = G-E
        h0 = D-B
        h1 = H-F
        I = 0
        if a[3] - a[0] <  w0 + w1 and  b[3] - b[0] < h0 + h1:
            I = (a[2] - a[1]) * (b[2] - b[1])
        print(a ,b, I)
        print(w0, h0, w1, h1)
        return w0 * h0 + w1 * h1 - I


# @lc code=end
tmp = Solution().computeArea(-2,-2,2,2,3,3,4,4)
print(tmp)

