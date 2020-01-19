#
# @lc app=leetcode.cn id=332 lang=python3
#
# [332] 重新安排行程
#
from typing import *
# @lc code=start
from collections import defaultdict
from copy import deepcopy
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import defaultdict
        graph = defaultdict(list)
        airports = defaultdict(int)
        res = []
        for x, y in tickets:
            graph[x].append(y)
            # 记录x到y次数
            airports[x + y] += 1
        print(graph)

        def dfs(i, tmp, airports):
            nonlocal res

            if len(tmp) == len(tickets) + 1:
                res = tmp
                return
            for j in sorted(graph[i]):
                if airports[i + j] > 0 and not res:
                    airports[i + j] -= 1
                    dfs(j, tmp + [j], airports)
                    airports[i + j] += 1

        dfs("JFK", ["JFK"], airports)

        return res

# @lc code=end

tmp = Solution().findItinerary([["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]])

print(tmp)