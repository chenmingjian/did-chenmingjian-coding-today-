#
# @lc app=leetcode.cn id=1189 lang=python3
#
# [1189] “气球” 的最大数量
#

# @lc code=start
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c = collections.Counter(text)
        ans = []
        for i in 'balon':
            if i not in c:
                return 0
            if i in 'lo':
                ans.append(c[i] // 2)
            ans.append(c[i])
        return min(ans)
# @lc code=end

