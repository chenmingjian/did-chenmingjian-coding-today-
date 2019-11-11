#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
from typing import *
# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        r, n = [[n**2]], n**2
        while n > 1:
             n, r = n - len(r), [[*range(n - len(r), n)]] + [*zip(*r[::-1])]
             print(r)
        return r
# @lc code=end
tmp = Solution().generateMatrix(3)
