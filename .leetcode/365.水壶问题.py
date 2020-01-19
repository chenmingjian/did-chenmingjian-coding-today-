#
# @lc app=leetcode.cn id=365 lang=python3
#
# [365] 水壶问题
#

# @lc code=start
class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        global hcf
        if x + y < z:
            return False
        smaller = min(x, y)
        for i in range(1, smaller+1):
            if x % i == 0 and y % i == 0:
                hcf = i  # 存在更大的值时会覆盖原来的hcf，最后剩下最大公约数
        if z % hcf == 0:
            return True
        return False
# @lc code=end

