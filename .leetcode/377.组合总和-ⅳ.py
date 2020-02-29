#
# @lc app=leetcode.cn id=377 lang=python3
#
# [377] 组合总和 Ⅳ
#
from typing import *
import itertools
import collections
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums = sorted(list(set(nums)))

        d = collections.defaultdict(int)
        for i in nums:
            d[i]+= 1
        
        def ok(t, init=False):
            print(t)
            if t not in d or init:
                for i in nums:
                    if i > t:
                        break
                    a = ok(t - i)
                    d[t] += a
            return d[t]
        for i in nums:
            ok(i, init=True)
        # print(d)
        # print(ok(target))
        # print(d)
        return ok(target)
# @lc code=end

tmp = Solution().combinationSum4([1,50], 200)
print(tmp)