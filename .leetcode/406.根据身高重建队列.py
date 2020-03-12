#
# @lc app=leetcode.cn id=406 lang=python3
#
# [406] 根据身高重建队列
#
from typing import *
# @lc code=start
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        print(people)
        output = []
        for p in people:
            output.insert(p[1], p)
            
        return output


            
# @lc code=end

Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
)