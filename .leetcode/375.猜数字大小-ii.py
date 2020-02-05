#
# @lc app=leetcode.cn id=375 lang=python3
#
# [375] 猜数字大小 II
#

# @lc code=start
import functools
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @functools.lru_cache(None)
        def ok(l, h):
            if (l >= h):
                return 0
            min_res = float('inf')
            for i in range(l, h+1):
                res = i + max(ok(i+1, h), ok(l, i-1))
                min_res = min(res, min_res)
            return min_res

        return ok(1, n)
# @lc code=end


