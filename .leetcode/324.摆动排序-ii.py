#
# @lc app=leetcode.cn id=324 lang=python3
#
# [324] 摆动排序 II
#
from typing import *
# @lc code=start
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(reverse=True)
        mid = len(nums) // 2
        nums[1::2],nums[0::2] = nums[:mid], nums[mid:]


# @lc code=end
a = [1,1,2,1,2,2,1]
Solution().wiggleSort(a)

print(a)

