#
# @lc app=leetcode.cn id=1514 lang=python3
#
# [1514] 概率最大的路径
#

# @lc code=start
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        ne = collections.defaultdict(list)
        for index, e in enumerate(edges):
            ne[e[0]].append([e[1], succProb[index]])    
            ne[e[1]].append([e[0], succProb[index]])  

        max_prob = [0 for i in range(n)]
        s = [(start, 1)]
        while s:
            new_s = []
            for node, prob in s:
                for j in ne[node]:
                    this_prob = prob*j[1]
                    if this_prob > max_prob[j[0]]:
                        max_prob[j[0]] =this_prob
                        new_s.append([j[0], this_prob])
            s = new_s
        print(max_prob)
        return max_prob[end]

# @lc code=end

