#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] 除法求值
#
from typing import *
# @lc code=start
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        chars = set()
        for i, j in equations:
            chars.add(i)
            chars.add(j)
        
        chars = sorted(list(chars))
        print(chars)
        matrix = [[0 for i in range(len(chars))] for i in range(len(chars))]

        for e, v in zip(equations, values):
            i_start = chars.index(e[0])
            i_end = chars.index(e[1])
            matrix[i_start][i_end] = v
        for i in range(len(chars)):
            matrix[i][i] = 1
        for i in range(len(chars)):
            for j in range(len(chars)):
                if matrix[i][j] != 0:
                    matrix[j][i] = 1/matrix[i][j]

        for i in matrix:
            print(i)

        def dfs(s, e, uesd=set()):
            print(s, e, uesd)
            uesd.add(s)
            uesd.add(e)
            for i, v in enumerate(matrix[s]):
                if v != 0:
                    if i == e:
                        return v
                    elif i not in uesd:
                        uesd.add(i)
                        ret =dfs( i, e, uesd=uesd)
                        if ret is None:
                            continue
                        return ret * v

        ans = []         
        for i, j in queries:
            if i not in chars or j not in chars:
                ans.append(-1)
                continue
            res = dfs(chars.index(i), chars.index(j), set())

            ans.append(res if res is not None else -1)
            print(ans)
            # break
        print(ans)
        return ans
# @lc code=end

Solution().calcEquation([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]], [3.0,4.0,5.0,6.0], [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]])

