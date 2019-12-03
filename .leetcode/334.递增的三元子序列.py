#
# @lc app=leetcode.cn id=334 lang=python3
#
# [334] 递增的三元子序列
#
from typing import *
# @lc code=start
class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:       
        if len(nums) < 3:
            return False

        win = [nums[0]]

        for num in nums:

            if num > win[-1]:
                win.append(num)
                if len(win) >= 3:
                    return True
            else:
                i = len(win) - 1
                while i > 0:
                    if win[i-1] < num:
                        break
                    i -= 1
                
                win[i] = num
            print(win)
        return False
# @lc code=end

tmp = Solution().increasingTriplet([2,5,3,4,5])
print(tmp)