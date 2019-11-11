#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = list(set(candidates))
        c = sorted(candidates)
        d = {}
        def sub(t):
            a= []
            for i in c:
                if i > t:
                    break 
                elif i == t:
                    a.append([i])
                else:
                    if t - i not in d:
                        d[t-i] = sub(t-i)
                    a += [ [i] + j for j in d[t-i]]
            return a
                    
        ans = set()
        for i in sub(target):
            i.sort()
            ans.add(tuple(j for j in i))
        print(ans)
        return ans
# @lc code=end

