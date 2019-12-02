#
# @lc app=leetcode.cn id=318 lang=python3
#
# [318] 最大单词长度乘积
#
# https://leetcode-cn.com/problems/maximum-product-of-word-lengths/description/
#
# algorithms
# Medium (59.16%)
# Likes:    55
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 6.5K
# Testcase Example:  '["abcw","baz","foo","bar","xtfn","abcdef"]'
#
# 给定一个字符串数组 words，找到 length(word[i]) * length(word[j])
# 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。
# 
# 示例 1:
# 
# 输入: ["abcw","baz","foo","bar","xtfn","abcdef"]
# 输出: 16 
# 解释: 这两个单词为 "abcw", "xtfn"。
# 
# 示例 2:
# 
# 输入: ["a","ab","abc","d","cd","bcd","abcd"]
# 输出: 4 
# 解释: 这两个单词为 "ab", "cd"。
# 
# 示例 3:
# 
# 输入: ["a","aa","aaa","aaaa"]
# 输出: 0 
# 解释: 不存在这样的两个单词。
# 
#
from typing import *
import string
# @lc code=start
class Solution():
    def maxProduct(self, words: List[str]) -> int:
        # 直观的版本，主要通过位运算来判断字母位
        # max_len = {}
        # for word in words:
        #     flag = 0  # flag用26位二进制表示该词使用了的字母
        #     for alp in word:
        #         flag |= 1 << ord(alp) - 97  # 置字母对应的二进制位为1
        #     max_len[flag] = max(max_len.get(flag, 0), len(word))  # 更新当前flag的最大长度
        # [0]用来避免对空列表取max，下面的比较次数为n^2
        # return max([0] + [max_len[x] * max_len[y] for x in max_len for y in max_len if x & y == 0])
        
        # 效率优化版，总比较次数少于n^2/2
        max_len, res = {}, 0
        for word in words:
            flag = 0  # flag用26位二进制表示该词使用了的字母
            for alp in word:
                flag |= 1 << ord(alp) - 97  # 置字母对应的二进制位为1
            _old = max_len.get(flag, 0)
            if len(word) > _old:  # 发现长度更新才做比较，减小运算量
                # 找到与当前flag不相交的最大长度，用来更新当前答案
                res = max(res, len(word)*max([0]+[max_len[i] for i in max_len if not i & flag]))
                max_len[flag] = len(word)  # 更新答案后再写入，减少遍历时碰到自己的这一次
        return res
# @lc code=end
tmp = Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
print(tmp)