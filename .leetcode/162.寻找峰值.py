#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def search(l, r):
            if l == r:
                return l
            mid = (l+r) // 2
            if nums[mid] > nums[mid+1]:
                return search(l, mid)
            else:
                return search(mid+1, r)

        return search(0, len(nums)-1)
# @lc code=end

