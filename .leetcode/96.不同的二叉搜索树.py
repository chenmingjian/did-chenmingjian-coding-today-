#
# @lc app=leetcode.cn id=96 lang=python3
#
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
           0
        all_node = list(range(1, n+1))

        d = {0:1, 1:1, 2:2}
        def ok(av):
            l = len(av)
            if l in d:
                return d[l]
            
            c = []
            for i in range(l):
                a = ok(av[:i])
                b = ok(av[i+1:])
                c.append(a*b)
            d[l] = sum(c)
            return d[l]

        tmp = ok(all_node)
        return tmp

# @lc code=end

