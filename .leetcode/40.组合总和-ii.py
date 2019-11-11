#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#
from typing import *
import collections
# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        c = sorted(candidates)
        d = {}
        def sub(t):
            a= set()
            for i in c:
                if i > t:
                    break 
                elif i == t:
                    a.add(tuple([i]))
                else:
                    if t - i not in d:
                        d[t-i] = sub(t-i)
                    a = a | set([tuple([i]) + j for j in d[t-i]])
            return a
        c_pole = collections.Counter(candidates)            
        ans = set()
        for i in sub(target):
            i = sorted(i)
            t = tuple(j for j in i)
            c1 = collections.Counter(t)
            for k in c1:
                if c1[k] > c_pole[k]:
                    break
            else:
                ans.add(t)
        print(ans)
        return ans
# @lc code=end

tmp = Solution().combinationSum2([10,1,2,7,6,1,5], 8)