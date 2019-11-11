#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
from typing import *
# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[999 for j in range(i+1)] for i in range(len(triangle) - 1)] + [triangle[-1]]
        
        def ok(i, j):
            if dp[i][j] != 999:
                return dp[i][j]
            else:
                print(i, j)
                dp[i][j] = min(ok(i+1, j), ok(i+1, j+1)) + triangle[i][j]
                return dp[i][j]
        ans = ok(0, 0)
        
        return ans 
        
# @lc code=end

Solution().minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])