#
# @lc app=leetcode.cn id=60 lang=python3
#
# [60] 第k个排列
#

# @lc code=start
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        c = 1
        for i in itertools.permutations([i for i in range(1, n+1)]):
            if c == k:
                return ''.join([str(j) for j in i])
            else:
                c+= 1
# @lc code=end

