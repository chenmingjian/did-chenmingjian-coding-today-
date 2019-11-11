#
# @lc app=leetcode.cn id=36 lang=python3
#
# [36] 有效的数独
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import numpy as np 
        b = np.array(board)
        bt = b.T

        rows = [[] for i in range(9)]
        columns = [[] for i in range(9)]
        cells = [[] for i in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    box_index = (i // 3) * 3 + j // 3
                    n = int (board[i][j])
                    if n not in rows[i]:
                        rows[i].append(n)
                    else:
                        return False
                    if n not in columns[j]:
                        columns[j].append(n)
                    else:
                        return False    
                    if n not in cells[box_index]:
                        cells[box_index].append(n)
                    else:
                        return False
        return True

                    
                
# @lc code=end

