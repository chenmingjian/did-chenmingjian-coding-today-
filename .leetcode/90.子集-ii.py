#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#

# @lc code=start
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(nums)+1):
            ans |= set(tuple(sorted(i)) for i in itertools.combinations(nums, i))

        return ans
# @lc code=end

