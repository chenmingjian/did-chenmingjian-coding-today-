#
# @lc app=leetcode.cn id=1217 lang=python3
#
# [1217] 
#

# @lc code=start
class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        c = collections.Counter(chips)
        print(c)
        a = sum([c[i] for i in c if i % 2 == 0])
        b = sum([c[i] for i in c if i % 2 != 0])
            
        return min(a, b)
# @lc code=end

