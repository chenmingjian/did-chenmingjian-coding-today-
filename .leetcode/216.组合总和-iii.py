#
# @lc app=leetcode.cn id=216 lang=python3
#
# [216] 组合总和 III
#
from typing import *
import itertools
# @lc code=start
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        for i in itertools.combinations(range(1, 10), k):
            if sum(i) == n:
                ans.append(i)

        return ans
# @lc code=end

Solution().combinationSum3(3, 7)