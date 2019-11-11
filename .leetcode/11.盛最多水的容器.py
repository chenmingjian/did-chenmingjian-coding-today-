#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ = 0
        l = 0
        r = len(height) - 1
        while l < r:
            max_ = max(max_, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_
        
# @lc code=end

Solution().maxArea([i for i in range(150001)])
