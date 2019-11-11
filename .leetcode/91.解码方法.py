#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        if s == '0':
            return 0
        d = {}
        def ok(s):
            if len(s) == 0:
                return 1
            if s[0] == '0':
                return 0
            if len(s) == 1:
                return 1
            i = int(s[0:2])
            
            if i <= 26:
                if s[2:] not in d:
                    d[s[2:]] = ok (s[2:])
                if s[1:] not in d:
                    d[s[1:]] = ok(s[1:])
                return  d[s[2:]] + d[s[1:]]
            else:
                if s[1:] not in d:
                    d[s[1:]] = ok(s[1:])
                return d[s[1:]]

        return ok(s)

# @lc code=end

