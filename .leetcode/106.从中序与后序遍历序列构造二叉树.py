#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def ok(p, i):
            # print(p, i)
            
            if len(p) == 0:
                return 

            node = TreeNode(p[-1])
            index = i.index(p[-1])

            # print('    ', p[-(len(i) - index):-1], i[index+1:])
            node.right = ok(p[-(len(i) - index):-1], i[index+1:])
            # assert(len(p[-(1+index):-1]) == len(i[index+1:]))

            # print('    ', p[:len(i[:index])], i[:index])
            node.left = ok(p[:len(i[:index])], i[:index])
            # assert( len(p[:-(1+index)]) == len(i[:index]))


            return node

        return ok(postorder, inorder)
# @lc code=end

