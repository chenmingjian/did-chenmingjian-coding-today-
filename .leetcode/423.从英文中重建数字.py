#
# @lc app=leetcode.cn id=423 lang=python3
#
# [423] 从英文中重建数字
#

# @lc code=start
from typing import *
from collections import Counter
import numpy as np
import scipy as sp
import scipy.linalg
import string
class Solution:
    def originalDigits(self, s: str) -> str:
        alphabet = string.ascii_lowercase
        num_str_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        num_str_len_list = [len(s) for s in num_str_list]
        num_counter_list = [Counter(i) for i in num_str_list]
        
        s_len = len(s)
        s_counter = Counter(s)

        A = []
        b = []

        for C in num_counter_list:
            a = [C[char] for char in alphabet]
            A.append(a)
        b += [s_counter[char] for char in alphabet]

        A = np.array(A).T
        b = np.array([b]).T

        pi_a = sp.linalg.pinv(A)
        s = pi_a.dot(b)

        ans =""
        for i, n in enumerate(s):
            print(i, n[0])
            if n[0] > 1e-5:
                print(' ', str(i) * int(round(n[0])))
                ans += str(i) * int(round(n[0]))
        print(ans)
        return ans

# @lc code=end

Solution().originalDigits("owoztneoer")