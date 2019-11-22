#
# @lc app=leetcode.cn id=289 lang=python3
#
# [289] 生命游戏
#
from typing import *
# @lc code=start
import copy
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        nn = len(board[0])
        def check(i, j):
            eight = [[i-1, j-1] ,[i-1, j], [i-1, j+1],
                     [i, j-1], [i, j+1],
                     [i+1, j-1], [i+1, j], [i+1, j+1]]
            c = 0
            for i, j in eight:
                print((i ,j))
                if i >= 0 and i < m and j >= 0 and j < nn:
                    print(board[i][j], board)
                    if board[i][j] == 1:
                        c += 1
            return c

        new = copy.deepcopy(board)
        for ii in range(m):
            print(ii, '!!!!!!!!!!!!!!')
            for ji in range(nn):
                print(ji, '???????????????')
                print(ii, ji)
                n = check(ii, ji)
                print(board[ii][ji], n)
                if board[ii][ji] == 1:
                    if n < 2:
                        new[ii][ji] = 0
                    elif n == 2 or n ==3:
                        new[ii][ji] = 1
                    else:
                        new[ii][ji] = 0
                else:
                    if n == 3:
                        new[ii][ji] = 1

        for i in range(m):
            for j in range(nn):
                board[i][j] = new[i][j] 

# @lc code=end

Solution().gameOfLife([[]])