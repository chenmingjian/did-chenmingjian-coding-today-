#
# @lc app=leetcode.cn id=1232 lang=python3
#
# [1232] 缀点成线
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        delta = [[i[0]-j[0], i[1] - j[1]] for i, j in zip(coordinates, coordinates[1:])]
        for i in delta[1:]:
            if delta[0][0] * i[1] != delta[0][1] * i[0]:
                return False
        return True 
# @lc code=end

