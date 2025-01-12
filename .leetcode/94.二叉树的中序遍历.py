#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        def ok(node):
            if node is None:
                return
            ok(node.left)
            ans.append(node.val)
            ok(node.right)
        ok(root)
        return ans4
        
# @lc code=end

