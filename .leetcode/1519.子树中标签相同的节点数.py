#
# @lc app=leetcode.cn id=1519 lang=python3
#
# [1519] 子树中标签相同的节点数
#
from typing import *
import collections

# @lc code=start
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        adjaction_matrix = collections.defaultdict(list)
        for i, j in edges:
            adjaction_matrix[i].append(j)
            adjaction_matrix[j].append(i)
        res = [1 for i in range(n)]

        d = collections.defaultdict(int)

        def dfs(node, path):
            # print(node, path)
            for i in path:
                if labels[node] == labels[i]:
                    res[i] += 1
            for i in adjaction_matrix[node]:
                if i not in path:
                    d[]
                    path.append(node)
                    dfs(i, path)
                    path.pop()

        dfs(0, [])
        return res
# @lc code=end
print(Solution().countSubTrees(n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"))
