#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
from typing import *
# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        a = [0 for i in nums]

        for i in range(1, len(nums)):
            l = []
            for j in range(1, i + 1):
                if nums[i - j] < nums[i]:
                    l.append(a[i-j])
            a[i] = max(l) + 1 if len(l) != 0 else 0
        print(nums)
        print(a)
        return max(a) + 1
            
# @lc code=end

tmp = Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])
print(tmp)