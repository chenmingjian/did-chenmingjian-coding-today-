#
# @lc app=leetcode.cn id=397 lang=python3
#
# [397] 整数替换
#
from typing import *
# @lc code=start
class Solution:
    def integerReplacement(self, n: int) -> int:
        d = {1:0}

        def ok(num):
            
            if num not in d:
                if num % 2 == 0:

                    d[int(num)] = ok(num/2) + 1
                else:
                    d[int(num)] = min(ok(num+1), ok(num-1)) + 1
            
            return d[num]
        c = ok(n)
        # print(d)
        # print(c)
        return c
# @lc code=end

Solution().integerReplacement(65535)