#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = sorted(nums)

        sum_ = sum(n[:3])
        for k, a in enumerate(n):
            # if a >= target:
            #     break
            i = k+1
            j = len(n) - 1
            while i < j:
                s = a + n[i] + n[j]
                print(s)
                if abs(s - target) < abs(target - sum_):
                    sum_ = s
                if s  < target:
                    i+=1
                elif target < s:
                    j-=1
                else:
                    return sum_
        
        return sum_
                    
                

# @lc code=end

