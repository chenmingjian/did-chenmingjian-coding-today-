#
# @lc app=leetcode.cn id=304 lang=python3
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (41.46%)
# Likes:    51
# Dislikes: 0
# Total Accepted:    3.8K
# Total Submissions: 9.3K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2)。
# 
# 
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 
# 示例:
# 
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 说明:
# 
# 
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2。
# 
# 
#

# @lc code=start
import numpy as np
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = np.array(matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return np.sum(self.m[row1:row2+1, col1:col2+1])


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

