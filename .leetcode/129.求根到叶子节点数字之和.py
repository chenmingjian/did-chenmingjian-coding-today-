#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根到叶子节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        ans = []
        def ok(node, path = []):
            if node is None:
               return 

            path = path.copy()
            path.append(node.val)
            if node.left is None and node.right is None:
                ans.append(path)
                return 
            ok(node.left, path)
            ok(node.right, path)
        ok(root)
        print(ans)

        def list2i(l):
            s = '0'
            for i in l:
                s += str(i)
            return int(s)


        a = [list2i(i) for i in ans]
        return sum(a) if len(a) != 0 else 0


         
# @lc code=end

