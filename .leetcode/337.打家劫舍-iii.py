#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:

        d = {}

        def ok(node):

            if node is None:
                return 0

            if node in d:
                return d[node]
            a = []
            if node.left is not None:
                a.append(node.left.left)
                a.append(node.left.right)

            if node.right is not None:
                a.append(node.right.left)
                a.append(node.right.right)
            ans = 0
            for i in a:
                if i not in d:
                    d[i] = ok(i)
                ans += d[i]

            d[node] = max(node.val + ans, ok(node.left) + ok(node.right))
            return d[node]

        return ok(root)

# @lc code=end

