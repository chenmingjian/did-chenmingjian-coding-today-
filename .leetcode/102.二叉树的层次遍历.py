#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
            
        q = collections.deque()
        q.append((root, 0))

        a = []
        while q:
            node, level = q.popleft()
            if node is not None:
                if len(a) > level:
                    a[level].append(node.val)
                else:
                    a.append([node.val])
                q.append((node.left, level+1))
                q.append((node.right, level+1))

        return a
                
# @lc code=end

