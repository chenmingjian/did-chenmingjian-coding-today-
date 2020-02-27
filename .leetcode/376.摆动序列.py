#
# @lc app=leetcode.cn id=376 lang=python3
#
# [376] 摆动序列
#
from typing import *
# @lc code=start
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        count = 1
        last_gap = float('inf')
        this = nums[0]
        for i in nums[1:]:
            print(i)
            if last_gap == float('inf'):
                if i == this:
                    continue
                last_gap = i - this
                count += 1
                this = i
                continue
            this_gap = i - this
            print('i=%d'%i, 'this=%d'%this, this_gap)
            this = i
            print(last_gap, this_gap)
            if (this_gap > 0 and last_gap < 0) or\
                (this_gap < 0 and last_gap > 0):
                count = count + 1
            else:
                continue
            last_gap = this_gap
        return count
# @lc code=end
a = Solution().wiggleMaxLength([3,3,3,2,5])
print(a)