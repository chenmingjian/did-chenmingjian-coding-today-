#
# @lc app=leetcode.cn id=424 lang=python3
#
# [424] 替换后的最长重复字符
#
from typing import *
# @lc code=start
import string
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letter_num = {}
        l = 0
        res = 0
        for r in range(len(s)):
            letter_num[s[r]] = letter_num.get(s[r], 0) + 1
            max_letter = max(letter_num, key=letter_num.get)
            while r - l+1 -letter_num[max_letter] > k:
                letter_num[s[l]] -= 1
                l += 1
                max_letter = max(letter_num, key=letter_num.get)

            res = max(res, r-l+1)

        return res
            
# @lc code=end

Solution().characterReplacement("AABABBA", 1)