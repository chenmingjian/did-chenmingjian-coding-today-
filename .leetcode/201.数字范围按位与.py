#
# @lc app=leetcode.cn id=201 lang=python3
#
# [201] 数字范围按位与
#

# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        t = 0
        while m != n:
            m >>= 1
            n >>= 1
            t += 1
        return n << t

# @lc code=end

