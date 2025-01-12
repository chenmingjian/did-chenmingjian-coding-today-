#
# @lc app=leetcode.cn id=306 lang=python3
#
# [306] 累加数
#
# https://leetcode-cn.com/problems/additive-number/description/
#
# algorithms
# Medium (31.60%)
# Likes:    43
# Dislikes: 0
# Total Accepted:    2.9K
# Total Submissions: 9K
# Testcase Example:  '"112358"'
#
# 累加数是一个字符串，组成它的数字可以形成累加序列。
# 
# 一个有效的累加序列必须至少包含 3 个数。除了最开始的两个数以外，字符串中的其他数都等于它之前两个数相加的和。
# 
# 给定一个只包含数字 '0'-'9' 的字符串，编写一个算法来判断给定输入是否是累加数。
# 
# 说明: 累加序列里的数不会以 0 开头，所以不会出现 1, 2, 03 或者 1, 02, 3 的情况。
# 
# 示例 1:
# 
# 输入: "112358"
# 输出: true 
# 解释: 累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
# 
# 
# 示例 2:
# 
# 输入: "199100199"
# 输出: true 
# 解释: 累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
# 
# 进阶:
# 你如何处理一个溢出的过大的整数输入?
# 
#
from typing import *
# @lc code=start
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def ok(l, last=[]): 
            last = last.copy()

            print(l, last)
            if l == '':
                return True
            if len(last) == 2:
                s = sum(last)
                sum_len = len(str(s))
                if l[:sum_len] == str(s):
                    return ok(l[sum_len:], last[1:]+[s])
                else:
                    return False
            else:
                a = []
                for i in range(1, len(l)//2+1):
                    if l[:i][0] == '0' and i > 1:
                        continue
                    head_int = int(l[:i])
                    new = last + [head_int]
                    a.append((ok(l[i:], new)))
                return any(a)

        return ok(num)        
# @lc code=end

tmp = Solution().isAdditiveNumber("0235813")
print(1)
print(tmp)