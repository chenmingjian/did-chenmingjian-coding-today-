#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if board == []:
            return
        m = len(board)
        n = len(board[0])

        a = [[0, j] for j in range(n)]
        b = [[i, 0] for i in range(m)]
        c = [[i, n-1] for i in range(m)]
        d = [[m-1, j] for j in range(n)]
        print(m, n, a,b,c,d)
        hope = [i for i in a+b+c+d if board[i[0]][i[1]] == 'O']
        
        sh = set([tuple(i) for i in hope])
        while hope:
            hi, hj = hope.pop()

            # pass_the_flame = []

            candidates = [[hi + 1, hj], [hi-1, hj], [hi ,hj+1], [hi, hj-1]]
            for i, j in candidates:
                if i > 0 and i < m-1 and j > 0 and j < n-1:
                    if board[i][j] == 'O':
                        if tuple([i, j]) not in sh:
                            hope.append([i, j])
                            sh.add(tuple([i, j]))
        
        for i in range(m):
            for j in range(n):
                if tuple([i, j]) in sh:
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'



                
# @lc code=end

