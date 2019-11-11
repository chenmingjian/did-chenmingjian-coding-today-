#
# @lc app=leetcode.cn id=1103 lang=python3
#
# [1103] 分糖果 II
#

# @lc code=start
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        ans = [0] * num_people
        i = 0
        while candies > i:
            ans[i % num_people] += i + 1
            candies -= i + 1
            i += 1
        ans[i % num_people] += candies
        return ans
# @lc code=end

