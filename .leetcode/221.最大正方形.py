#
# @lc app=leetcode.cn id=221 lang=python3
#
# [221] 最大正方形
#
from typing import *
# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        max_ = 0
        def ok(i, j, k):
            check_list = [[a, j+k-1] for a in range(i, i+k)] + \
                         [[i+k-1, a] for a in range(j, j+k)]
            # print(check_list)
            for a, b in check_list:
                if a >= m or b >= n:
                    return False
                if matrix[a][b] != '1':
                    return False
            else:
                return True
        
        for i in range(m):
            for j in range(n):

                if matrix[i][j] == '1':
                    tmp = 2
                    while ok(i, j, tmp):
                        tmp += 1
                    max_ = max(max_, (tmp-1)**2)

        return max_
                    
# @lc code=end

tmp = Solution().maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]])
print(tmp)