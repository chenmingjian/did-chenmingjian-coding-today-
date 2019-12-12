#
# @lc app=leetcode.cn id=372 lang=python3
#
# [372] 超级次方
#

# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def pow(a,n) -> int:
            if n == 0: return 1
            if n == 1: return a
            return (pow(a, n//2) * pow(a, n - n//2)) % 1337
        ret = 1
        for i in b:
            ret = (pow(ret, 10) * pow(a, i)) % 1337

        return ret
# @lc code=end

