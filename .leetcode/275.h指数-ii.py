#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        i = 0
        while i<len(citations) and citations[len(citations)-1 - i] > i:
            i+= 1

        return i
        
# @lc code=end

