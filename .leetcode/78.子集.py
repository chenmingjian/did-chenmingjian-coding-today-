#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            ans += list(itertools.combinations(nums, i))

        return ans
        
# @lc code=end

