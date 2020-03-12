#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#
from typing import *
# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        res = []
        s, e = 0, 0
        diff = float('inf')
        for idx, (i, i_plus_1) in enumerate(zip(A, A[1:])):
            if diff == float('inf'):
                diff = i_plus_1 - i
            else:
                diff_now = i_plus_1 - i
                if diff_now == diff:
                    e = idx
                else:
                    diff = diff_now
                    res.append(A[s:e+2])
                    s = e = idx
        else:
            res.append(A[s:e+2])
        print(res)

        ans = 0
        for i in res:

            if len(i) >= 3:
                ans += sum([n for n in range(len(i)-1)])
        print(ans)
        return ans        
# @lc code=end

Solution().numberOfArithmeticSlices([1, 2, 3])