#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def n2s(n):
            s = ''
            while n != 0:
                a = n % 10 
                s = str(a) + s
                n = n // 10
            return s if len(s) != 0 else '0'
        def s2n(s):
            n = 0
            for i in s:
                n = n*10 + int(i)
            return n

        return n2s(s2n(num1) * s2n(num2))
        
# @lc code=end

tmp = Solution().multiply("123", "123")
print(tmp)