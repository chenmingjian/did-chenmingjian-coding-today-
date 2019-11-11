#
# @lc app=leetcode.cn id=1078 lang=python3
#
# [1078] Bigram 分词
#

# @lc code=start
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        s = text.split(" ")
        ok = 0
        ans = []
        for i in s:
            if ok == 2:
                ans.append(i)
                ok = 0
            if i == first:
                ok = 1
            if i == second and ok == 1:
                ok += 1
            if i != first and i != second:
                ok = 0
        return ans
                
# @lc code=end

