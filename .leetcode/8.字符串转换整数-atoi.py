#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        s = str.strip(' ')

        a = ''
        for i in s:
            if i.isdigit() or (a == '' and (i == '-' or i == '+')):
                a += i
            else:
                break
        
        if a == '-' or a == '+' or len(a) == 0:
            return 0

        tmp = int(a)
        if tmp > 2**31-1:
            return 2**31-1
        if tmp < -2**31:
            return -2**31
        return tmp
# @lc code=end

