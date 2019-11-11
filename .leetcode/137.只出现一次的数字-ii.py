#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#

# @lc code=start
import functools
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        b = functools.reduce(lambda x, y : x^ y, nums)
        return b
# @lc code=end

