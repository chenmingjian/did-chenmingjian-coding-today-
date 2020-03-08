#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
from typing import *
# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        
        def ok(sub_s):
            if sub_s == '':
                return ''
            # print(sub_s)
            this_part_str = ''
            this_count = '0'
            this_expose = ''
            start, end = 0, 0
            square_bracket_count = 0
            for i, c in enumerate(sub_s):
                
                if start == 0:
                    if str.isnumeric(c):
                        this_count += c
                    elif str.isalpha(c):
                        this_expose += c
                    elif c == '[':
                        start = i
                else:
                    if square_bracket_count == 0 and c == ']':
                        end = i
                        break
                    elif c == '[':
                        square_bracket_count += 1
                    elif c == ']':
                        square_bracket_count -= 1
            if start == 0 and end == 0:
                return this_expose
            inside = ok(sub_s[start+1:end])
            this_part_str = this_expose \
                + ''.join([inside for i in range(int(this_count))]) \
                + ok(sub_s[end+1:])
            # print('ans =', this_part_str)
            return this_part_str
        a = ok(s)
        print(a)
        return a
# @lc code=end

Solution().decodeString("3[a2[c]]")