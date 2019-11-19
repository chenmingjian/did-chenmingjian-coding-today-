#
# @lc app=leetcode.cn id=220 lang=python3
#
# [220] 存在重复元素 III
#

# @lc code=start
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        if t < 0:
            return False
        Set = {}
        for i in range(len(nums)):
            key = nums[i]//(t+1)
            if key in Set:
                Set[key].append(i)
                if Set[key][-1]-Set[key][-2] <= k:
                    return True
            else:
                Set[key] = [i]
            if key+1 in Set and Set[key+1][0]-Set[key][-1] <= k and abs(nums[Set[key+1][0]]-nums[Set[key][-1]]) <= t:
                return True
            if key-1 in Set and Set[key][0]-Set[key-1][-1] <= k and abs(nums[Set[key][0]]-nums[Set[key-1][-1]]) <= t:
                return True
        #print(Set)
                
        return False

# @lc code=end

