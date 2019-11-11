#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#
from typing import *
# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = {}

        def ok(a, b):
            if a == 1 or b == 1:
                return 1
            if tuple([min(a, b), max(a, b)]) not in d:
                d[tuple([min(a, b), max(a, b)])] = ok(a-1, b) + ok(a, b-1)
            return d[tuple([min(a, b), max(a, b)])]

        return ok(m, n)

# @lc code=end

print(Solution().uniquePaths(23, 12))