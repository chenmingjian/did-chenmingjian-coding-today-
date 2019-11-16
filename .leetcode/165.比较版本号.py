#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]

        while len(v1) < 3:
            v1.append(0)
        while len(v2) < 3:
            v2.append(0)

        for i, j in zip(v1, v2):
            if i < j:
                return -1
            elif i > j:
                return 1
        else:
            return 0
        
# @lc code=end

