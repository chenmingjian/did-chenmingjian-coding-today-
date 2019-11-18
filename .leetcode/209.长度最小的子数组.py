#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n=len(nums)
        l=0
        res=float("inf")
        tmp=0
        for r in range(n):
            tmp+=nums[r]
            while(tmp>=s):
                res=min(res,r-l+1)
                tmp-=nums[l]
                l+=1
        return res if(res!=float("inf")) else 0

                
# @lc code=end

