#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def ok(node):
            if node is None:
                return None

            if node.left is None and node.right is None:
                return node


            l = ok(node.left)
            node.left = None
            tmpr = node.right
            node.right = l

            n = node
            while n.right:
                n = n.right

            r = ok(tmpr)
            n.right = r

            return node

        ok(root)

        
# @lc code=end

