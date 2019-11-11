#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in itertools.permutations(nums):
            i = tuple([j for j in i])
            ans.add(i)
        return ans
# @lc code=end

