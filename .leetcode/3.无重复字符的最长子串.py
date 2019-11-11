#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
import collections
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        ans = []
        a = collections.OrderedDict()
        for index, c in enumerate(s):
            if c in a:
                ans.append(index - i)
                i = a[c]
                k, v = a.popitem(False)
                while i == k:
                    k, v = a.popitem(False)
            else:
                a[c] = index
            print(a)
        print(ans)
        return max(ans) if len(ans) != 0 else 0

# @lc code=end

