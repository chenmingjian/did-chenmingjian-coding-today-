#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
from typing import *
import itertools
# @lc code=start
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        f = [[0 if i!=j else 1  for i in range(len(s))]for j in range(len(s))]
        
        for j in range(1, len(s)):
            for i in range(0, len(s)-j):
                if j  == 1:
                    f[i][j+i] = 1 if s[i] == s[j+i] else 0
                else:
                    # print(i, j)
                    f[i][j+i] = 1 if f[i+1][j+i-1] == 1 and s[i] == s[j+i] else 0
        # print(f)
        ans = []
        def helper(start, path):
            if start >= len(s):
                ans.append(path.copy())
                return

            for i in range(len(s)):
                if f[start][i] == 1: 
                    left = s[start:i+1]
                    path.append(left)
                    helper(i+1, path)
                    path.pop()
        helper(0, [])

        return ans

# @lc code=end
print(Solution().partition("123321121")) 