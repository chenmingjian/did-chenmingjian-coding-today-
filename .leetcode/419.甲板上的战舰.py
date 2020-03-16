#
# @lc app=leetcode.cn id=419 lang=python3
#
# [419] 甲板上的战舰
#

# @lc code=start
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X' and (not i or board[i - 1][j] == '.') \
                    and (not j or board[i][j - 1] == '.'):
                    res += 1
        return res
# @lc code=end

