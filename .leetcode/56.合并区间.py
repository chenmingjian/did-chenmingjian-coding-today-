#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import *
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        while intervals:
            i = intervals.pop()
            for j in intervals:
                if i[1] >= j[0] and j[1] >= i[0]:
                    i[0] = min(i[0], j[0])
                    i[1] = max(i[1], j[1])
                    intervals.remove(j)
                    intervals.append(i)
                    break
            else:
                ans.append(i)

        return ans
# @lc code=end

tmp = Solution().merge([[1,3],[2,6],[8,10],[15,18]])

print(tmp)
