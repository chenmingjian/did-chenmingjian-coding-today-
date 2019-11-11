#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:    
        a = [0, 1, 1]
        if n < 3:
            return a[n]
        for i in range(3, n):
            a.append(sum(a))
            a = a[1:]
        return sum(a)
# @lc code=end

