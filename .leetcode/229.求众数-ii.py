#
# @lc app=leetcode.cn id=229 lang=python3
#
# [229] 求众数 II
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        return [k for k in c if c[k] > len(nums) // 3]
                
# @lc code=end

