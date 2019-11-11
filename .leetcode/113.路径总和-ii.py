#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def ok(node, path = []):
            if node is None:
                return 

            path.append(node.val)
            if node.left is None and node.right is None:
                ans.append(path) 
                # path.pop()
                return 
            ok(node.left, path.copy())

            ok(node.right, path.copy())



        ok(root)
        def addall(x):
            r = 0
            for i in x:
                r += i
            return r
        return [i for i in ans if addall(i) == sum]          

# @lc code=end

