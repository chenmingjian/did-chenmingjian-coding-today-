#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#
import itertools
from typing import *
# @lc code=start

import re
import operator  

class Solution:
    def diffWaysToCompute(self, input):
        items = re.split('(\D)', input)
        print(items)
        nums = list(map(int, items[::2]))
        ops = list(map({'+':operator.add, '-':operator.sub, '*':operator.mul}.get, items[1::2]))
        def calc(low, high):
            if low == high:
                return [nums[low]]
            return [ops[i](a, b)
               for i in range(low, high)
               for a in calc(low, i)
               for b in calc(i + 1, high)]
        return calc(0, len(nums)-1)
# @lc code=end

print(Solution().diffWaysToCompute("2*3*3"))