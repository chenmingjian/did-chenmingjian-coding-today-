#
# @lc app=leetcode.cn id=433 lang=python3
#
# [433] 最小基因变化
#

# @lc code=start
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        from collections import deque
        bank = set(bank)
        if end not in bank:
            return -1
        visited = set()
        visited.add(start)
        mutations = {'A', 'C', 'G', 'T'}

        def oneMuation(cur):
            for i, val in enumerate(cur):
                for t in mutations - {val}:
                    tmp = cur[:i] + t + cur[i+1:]
                    if tmp in bank:
                        yield tmp

        q = deque([[start, 0]])
        while q:
            cur, res = q.pop()
            if cur == end:
                return res
            for n in oneMuation(cur):
                if n not in visited:
                    visited.add(n)
                    q.appendleft([n, res + 1])
        return -1

# @lc code=end

