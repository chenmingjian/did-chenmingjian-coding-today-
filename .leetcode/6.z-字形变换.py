#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        a = ["" for i in range(numRows)]
        b = [i for i in range(numRows)]
        b += b[::-1][1:-1]
        print(b)
        for index, i in enumerate(s):
            index = b[index % len(b)]
            a[index] += i
        print(a)
        ans = ''
        for i in a:
            ans += i
        return ans

# @lc code=end

