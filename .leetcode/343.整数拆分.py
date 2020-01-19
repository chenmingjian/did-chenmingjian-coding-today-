#
# @lc app=leetcode.cn id=343 lang=python3
#
# [343] 整数拆分
#
from typing import *
# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3: return n - 1
        a, b = divmod(n, 3)
        if b == 0: return 3 ** a
        if b == 1: return 3 ** (a - 1) * 4
        return 3 ** a * 2
# @lc code=end

tmp = Solution().integerBreak(2)
print(tmp)
