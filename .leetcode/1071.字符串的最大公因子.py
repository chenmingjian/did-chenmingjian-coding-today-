#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071]
#

# @lc code=start


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if(len(str2)>len(str1)):
            return self.gcdOfStrings(str2,str1)
        s=str1.replace(str2,"")
        if s=="":
            return str2
        elif s==str1:
            return ""
        else:
            return self.gcdOfStrings(str2,s)

# @lc code=end
