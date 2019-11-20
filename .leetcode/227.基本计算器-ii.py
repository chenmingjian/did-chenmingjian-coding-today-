#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
from typing import *
# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join([i for i in s if i != ' '])

        n = []
        op = []
            
                # if i == '*':
                #     n.append(int(this) * n.pop())
                    
                # elif i == '/':
                #     n.append(int(this) // n.pop())
        this = ''
        for i in s:
            if i not in ['+', '-', '*', '/']:
                this += i
            else:
                n.append(int(this))
                op.append(i)
                this = ''
        
        n.append(int(this))
        n = n[::-1]
        op = op[::-1]
        print(n, op)
        n1 = []
        op1 = []
        while op:
            o = op.pop()
            if o == '*':
                a = n.pop()
                b = n.pop()
                n.append(a * b)
            elif o == '/':
                a = n.pop()
                b = n.pop()
                n.append(a // b)
            else:
                n1.append(n.pop())
                op1.append(o)
        n1.append(n.pop())
        n = n1[::-1]
        op  = op1[::-1]
        print(n, op)
        while op:
            o = op.pop()
            a = n.pop()
            b = n.pop()
            if o == '+':
                n.append(a + b)
            elif o == '-':
                n.append(a - b)

        return n.pop()
# @lc code=end

tmp = Solution().calculate("0-2147483647")
print(tmp)