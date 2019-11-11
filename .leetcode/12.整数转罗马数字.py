#
# @lc app=leetcode.cn id=12 lang=python3
#
# [12] 整数转罗马数字
#

# @lc code=start


class Solution:
    def intToRoman(self, num: int) -> str:
        a = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 900:"CM", 400:'CD', 40:'XL', 90:'XC', 9:'IX', 4:'IV'}
        sk = sorted(a.keys(), reverse=True)
        ans = ''
        while num > 0:
            for i in sk:
                if num >= i:
                    num -= i
                    ans += a[i]
                    break

        return ans

# @lc code=end
