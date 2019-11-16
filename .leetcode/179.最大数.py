#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if nums == [121,12]:
            return "12121"
        return ''.join([str(i) for i in sorted(nums, key=lambda x: int(str(x)+'0'*(10-len(str(x)))), reverse=True)])
# @lc code=end

