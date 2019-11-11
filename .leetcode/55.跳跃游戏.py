#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from typing import *
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = 0
        n = len(nums)
        while start <= end and end < len(nums) - 1:
            end = max(end, nums[start] + start)
            start += 1
        return end >= n - 1
# @lc code=end

tmp = Solution().canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])
print(tmp)