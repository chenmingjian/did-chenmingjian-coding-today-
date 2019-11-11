#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
from typing import *
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def p(n):
            print(n)
            if len(n) == 1:
                return n
            a = []
            for i in n:
                
                w = n.copy()
                w.remove(i)
                t = p(w)
                a.append([i] + j for j in )
            print(a)
            return a
        return p(nums)
# @lc code=end

tmp = Solution().permute([1, 2, 3])

print(tmp)