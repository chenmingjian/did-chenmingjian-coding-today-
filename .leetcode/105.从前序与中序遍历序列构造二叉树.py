#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # p = preorder[::-1]
        
        def ok(p, i):
            if len(p) == 0:
                return 

            node = TreeNode(p[0])
            index = i.index(p[0])
            
            node.left = ok(p[1:1+index], i[:index])
            assert(len(p[1:1+index]) == len(i[:index]))
            node.right = ok(p[1+index:], i[index+1:])
            assert(len(p[1+index:]) == len(i[index+1:]))

            return node

        return ok(preorder, inorder)
# @lc code=end

