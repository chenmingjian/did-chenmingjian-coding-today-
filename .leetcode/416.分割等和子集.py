#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#
from typing import *
# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        target=sum(nums)
        if(target%2!=0):
            return False
        target//=2
        dp=[[False]*(target+1) for _ in range(n)]
        dp[0][0]=True
        for i in range(1,target+1):
            if(nums[0]==i):
                dp[0][i]=True
                break
        for i in range(1,n):
            for j in range(target+1):
                if(j>=nums[i]):
                    dp[i][j]=dp[i-1][j] or (dp[i-1][j-nums[i]])
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]



# @lc code=end

Solution().canPartition([1, 2, 3, 5])