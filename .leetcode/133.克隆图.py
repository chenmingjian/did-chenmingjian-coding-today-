#
# @lc app=leetcode.cn id=133 lang=python3
#
# [133] 克隆图
#
from typing import *
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        d = {}
        def dfs(n):
            if n not in d:
                d[n] = new = Node(n.val, None)
                new.neighbors = [*map(dfs, n.neighbors)]
            return d[n]

        return dfs(node)
        
# @lc code=end

