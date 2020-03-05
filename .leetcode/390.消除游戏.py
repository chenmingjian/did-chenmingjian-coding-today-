#
# @lc app=leetcode.cn id=390 lang=python3
#
# [390] 消除游戏
#
from typing import *
# @lc code=start
import math
class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 0:
            return 0
        
        first = 1
        factor = 1
        isLeft = True
        isEven = ((n&1) == 0)

        while n != 1:
            if isLeft or not isEven:
                first += factor
            isLeft = not isLeft
            n = n>>1
            factor <<= 1
            isEven = (n&1) == 0

        return first
        
# @lc code=end

tmp = Solution().lastRemaining(40250)
print(tmp)