#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        all_node = list(range(1, n+1))
        def ok(av):
            if len(av) == 0:
                return [None]
            node_list = []
            for i in range(0, len(av)):
                node = TreeNode(av[i])
                
                for j in ok(av[:i]):
                    
                    node.left = j

                    for k in ok(av[i+1:]):
                        node.right = k
                        node_list.append(node)
                        node = TreeNode(av[i])
                        node.left = j

            return node_list if len(node_list) != 0 else [None]

        tmp = ok(all_node)
        return tmp

            
# @lc code=end

