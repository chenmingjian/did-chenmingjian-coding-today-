#
# @lc app=leetcode.cn id=338 lang=python3
#
# [338] 比特位计数
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        ans = []
        for i in range(num+1):
            n = bin(i)[2:]
            count = len([1 for i in n if i == '1'])
            ans.append(count)

        return ans
        
        
# @lc code=end

