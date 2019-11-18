#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#
from typing import *
# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)

        d = {}
        def ok(l):
            if  len(l) == 0:
                return 0
            if len(l) == 1:
                return l[0]

            tmp1 = tuple(l[2:])
            if tmp1 not in d:
                d[tmp1] = ok(tmp1)

            tmp2 = tuple(l[1:])
            if tmp2 not in d:
                d[tmp2] = ok(tmp2)

            return max(l[0] + d[tmp1], d[tmp2])

        ans = max(ok(nums[1:]), ok(nums[:-1]))
        return ans
# @lc code=end
print(Solution().rob([94,40,49,65,21,21,106,80,92,81,679,4,61,6,237,12,72,74,29,95,265,35,47,1,61,397,52,72,37,51,1,81,45,435,7,36,57,86,81,72]))

