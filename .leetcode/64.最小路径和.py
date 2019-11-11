#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
from typing import *
# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        g = grid[::-1]
        g = [list(i) for i in zip(*g)][::-1]
        print(g)
        m, n = len(g), len(g[0])
        for i in range(1, n):
            g[0][i] += g[0][i-1]
        for i in range(1, m):
            g[i][0] += g[i-1][0]
        print(g)
        for i in range(1, m):
            for j in range(1, n):
                g[i][j] += min(g[i-1][j], g[i][j-1])

        print(g)
        return g[-1][-1]
        
# @lc code=end

Solution().minPathSum([[1,2,5],[3,2,1]])