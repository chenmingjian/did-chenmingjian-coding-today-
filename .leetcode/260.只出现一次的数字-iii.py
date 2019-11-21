#
# @lc app=leetcode.cn id=260 lang=python3
#
# [260] 只出现一次的数字 III
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 0
        for x in nums:
            s ^= x

        lowbit = s&-s
        a = 0
        b = 0

        for x in nums:
            if x & lowbit == lowbit:
                a ^= x
            else:
                b ^= x

        return [a, b]
# @lc code=end

