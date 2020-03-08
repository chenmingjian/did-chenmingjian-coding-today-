#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] 至少有K个重复字符的最长子串
#

# @lc code=start
class Solution():
    def longestSubstring(self, s, k):
        if len(s) < k:
            return 0
        # 获取出现次数最少的字符
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))

# @lc code=end

