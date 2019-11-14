#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#
from typing import *
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = []
        o = []
        for i in tokens:
            if str.isnumeric(i) or len(i)>=2:
                n.append(int(i))
            else:
                b = n.pop()
                a = n.pop()
                if i == '+':
                    n.append(a + b)
                elif i == '-':
                    n.append(a - b)
                elif i == '*':
                    n.append(a * b)
                elif i == '/':
                    n.append(int(a / b))
                else:
                    print(i, '?')

        return n.pop()
                    
                
# @lc code=end

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))