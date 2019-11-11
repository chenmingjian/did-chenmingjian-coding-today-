#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        a = []
        def inorderTranversal(node):
            if node is None:
                return 
            inorderTranversal(node.left)
            a.append(node.val)
            inorderTranversal(node.right)

        inorderTranversal(root)
        
        
        return a == sorted(set(a))


        
# @lc code=end

