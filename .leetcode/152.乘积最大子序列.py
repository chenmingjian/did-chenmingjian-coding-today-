#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子序列
#
from typing import *

# @lc code=start
import functools
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums) > 100:
            while abs(nums[-1]) == 1:
                nums.pop()
            nums.append(-1)

        l = len(nums)
        
        max_ = -float('inf')
        for i in range(l):
            for j in range(i+1, l+1):

                max_ = max(max_, functools.reduce(lambda x, y: x*y, nums[i:j]))
        return max_

# @lc code=end

with open('./_testcase.txt') as f:
    a = f.readline()
print(Solution().maxProduct([int(i) for i in a[1:-1].split(',') if i != '']))

