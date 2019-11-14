#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        a = []

        stack = [root]

        while stack:
            node = stack.pop()
            if node is not None:
                a.append(node.val)
                stack.append(node.right)
                stack.append(node.left)

        return a
# @lc code=end

