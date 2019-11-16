#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        a = []

        def ok(node, level):
            if node is None:
                return 
            if len(a) > level:
                a[level].append(node.val)
            else:
                a.append([node.val])
            ok(node.left, level+1)
            ok(node.right, level+1)
        ok(root, 0)
        return [ i.pop() for i in a ]
# @lc code=end

