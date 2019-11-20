#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#
from typing import *
# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        a = []
        for i in nums:
            if len(a) == 0:
                a.append([i, i])
                continue

            if i == a[-1][-1] + 1:
                a[-1][-1] += 1
            else:
                a.append([i, i])

        ans = []
        for i, j in a:
            if i == j:
                ans.append(str(i))
            else:
                ans.append(str(i)+'->'+str(j))

        return ans
# @lc code=end

tmp = Solution().summaryRanges([0,1,2,4,5,7])
print(tmp)