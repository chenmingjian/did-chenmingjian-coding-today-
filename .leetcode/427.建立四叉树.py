#
# @lc app=leetcode.cn id=427 lang=python3
#
# [427] 建立四叉树
#

# @lc code=start
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        import numpy as np
        grid = np.array(grid)
       
        def is_leaf(grid, row, col):
            return all(grid[i][j] == grid[0][0] for i in range(row) for j in range(col))
        
        def dfs(grid):
            row = len(grid)
            col = len(grid[0])
            if is_leaf(grid, row, col):
                return Node(
                    grid[0][0] == 1,
                    True,
                    None,None,None,None
                )
            root = Node(
                    "*", False, None,None,None,None
            )
            root.topLeft = dfs(grid[:row//2,:col//2])
            root.topRight = dfs(grid[:row//2, col//2:])
            root.bottomLeft = dfs(grid[row//2:,:col//2])
            root.bottomRight = dfs(grid[row//2:, col//2:])
            return root
            
        return dfs(grid)

# @lc code=end

