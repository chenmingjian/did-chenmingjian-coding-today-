#
# @lc app=leetcode.cn id=720 lang=python3
#
# [720] 词典中最长的单词
#

# @lc code=start
class Solution:
    def longestWord(self, words: List[str]) -> str:
        d = {"":0}
        a = sorted(words, key=len)
        for i in a:
            if i[:-1] in d:
                d[i] = 0
        
        ans = [i for i in d.keys() if ]
# @lc code=end

