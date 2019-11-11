#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        m = min(1000, len(s))
        a = [[0 for i in range(m+1)] for i in range(m+1)]
        ans = s[0]
        max_ = 0
        for j in range(1, m):
            for i in range(j):
                if s[i] == s[j] and ((j - i) <=2 or a[i+1][j-1] == 1):
                    a[i][j] = 1
                    if j - i + 1 > max_:
                        max_ = j - i + 1
                        ans = s[i:j+1]

        # print(a, max_) 

        return ans            

                    


# @lc code=end

