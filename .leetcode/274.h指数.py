#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H指数
#
from typing import *
# @lc code=start
import collections
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        d = {}
        c = collections.Counter(citations)

        for i in sorted(c.keys()):
            if len(d) == 0:
                d[i] = c[i]
                continue
            
            for j in d:
                d[j] += c[i]

            d[i] = c[i]
        ans = []
        for i in d:
            ans.append(min(i, d[i]))

        return max(ans) if len(ans) > 0 else 0
        
# @lc code=end

tmp = Solution().hIndex([0, 0, 4, 4])
print(tmp)