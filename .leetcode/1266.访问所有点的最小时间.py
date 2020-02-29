#
# @lc app=leetcode.cn id=1266 lang=python3
#
# [1266] 访问所有点的最小时间
#

# @lc code=start
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        this = points[0]
        for p in points[1:]:
            ans += max(abs(p[0] - this[0]), abs(p[1] - this[1]))
            this = p
        return ans 
            

# @lc code=end

