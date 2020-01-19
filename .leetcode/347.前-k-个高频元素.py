#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import collections
        c = collections.Counter(nums)

        return [i[0] for i in c.most_common(k)]

# @lc code=end

