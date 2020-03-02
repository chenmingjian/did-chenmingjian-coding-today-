#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

# @lc code=start
import numpy as np

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = np.array(matrix)
        m = m.flatten()
        m = sorted(m)
        return m[k-1]
# @lc code=end

