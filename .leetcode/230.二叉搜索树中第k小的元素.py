#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        a = []
        def ok(node):
            if node is None:
                return 
            a.append(node.val)
            ok(node.left)
            ok(node.right)

        ok(root)
        a.sort()
        return a[k-1] if k-1 < len(a) else -1
# @lc code=end

