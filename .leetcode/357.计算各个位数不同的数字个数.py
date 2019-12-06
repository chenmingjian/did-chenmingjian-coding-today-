#
# @lc app=leetcode.cn id=357 lang=python3
#
# [357] 计算各个位数不同的数字个数
#

# @lc code=start
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        res, muls = 10, 9
        for i in range(1, min(n,10)):
            muls *= 10 - i
            res += muls
        return res

# @lc code=end

