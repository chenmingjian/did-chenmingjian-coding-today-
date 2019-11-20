#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys
 
sys.setrecursionlimit(1000000) #例如这里设置为一百
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ap = []
        aq = []

        def ok(node, path=[]):
            if node is None or (aq != [] and ap != []):
                return
            path = path.copy()
            path.append(node)
            if node == p:
                ap.extend(path)
                print(ap)
            if node == q:
                aq.extend(path)
                print(aq)
            ok(node.left, path)
            ok(node.right, path)

        ok(root)
        ans = root
        print(len(ap), len(aq))
        for i, j in zip(ap, aq):
            if i == j:
                ans = i

        return ans


# @lc code=end

