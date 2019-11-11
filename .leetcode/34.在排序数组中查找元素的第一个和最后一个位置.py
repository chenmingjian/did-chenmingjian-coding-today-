#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, h = 0, len(nums) - 1
        while l < h:
            m = (l+h) // 2
            if target > nums[m]:
                l = m+1
            elif target < nums[m]:
                h = m-1
            else:
                break
        if l == h and nums[l] != target:
            return [-1, -1]
        a = b = (l+h) // 2
        while  a - 1 >= 0 and target == nums[a-1]: 
            a -= 1
        while b+1 <= len(nums)-1 and target == nums[b+1]: 
            b += 1

        return [a, b]
            
# @lc code=end

