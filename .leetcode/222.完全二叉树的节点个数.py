#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        self.c = 0
        def ok(node):
            if node is None:
                return 
            self.c += 1
            ok(node.left)
            ok(node.right)
        ok(root)
        return self.c
        
# @lc code=end

