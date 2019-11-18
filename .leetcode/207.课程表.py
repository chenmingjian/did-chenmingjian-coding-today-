#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for i in range(numCourses)]

        adjacency = [[] for i in range(numCourses)]

        queue = []

        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)

        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)

        while queue:
            pre = queue.pop(0)
            numCourses -= 1

            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)

        return not numCourses
            
        
# @lc code=end

