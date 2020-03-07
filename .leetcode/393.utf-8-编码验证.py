#
# @lc app=leetcode.cn id=393 lang=python3
#
# [393] UTF-8 编码验证
#
from typing import *
# @lc code=start
class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        data = list('{:0>8}'.format(i[2:]) for i in map(bin, data))
        print(data)
        this = 0

        for byte in data:
            if this == 0 or this == -1:
                if '10' == byte[:2]:
                    return False
                if '0' in byte:
                    bi = byte.index("0")
                    this = bi - 1
                    if this >= 4:
                        return False
                else:
                    return False

            elif this > 0:
                if '10' == byte[:2]:
                    this -= 1
                else:
                    return False
        return this == 0 or this == -1

# @lc code=end

tmp = Solution().validUtf8([115,100,102,231,154,132,13,10])
print(tmp)