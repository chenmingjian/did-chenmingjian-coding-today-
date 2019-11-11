#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
#
from typing import *
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return 
        this = nums[0]
        c = 1
        for index, i in enumerate(nums[1:]):
            print(this, i , c)
  
            if i == this:
                c += 1
            else:
                this = i
                c = 1
            if c > 2:
                nums[index+1] = float('inf')
        nums.sort()
        while nums[-1] == float('inf'):
            nums.pop()            
# @lc code=end
a = [1,1,1,2,2,3]
Solution().removeDuplicates(a)
print(a)
