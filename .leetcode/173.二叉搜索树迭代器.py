#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.l = []
        def dfs(node):
            if node is None:
                return 
            self.l.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        self.l.sort()
        self.i = -1

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.i += 1
            return self.l[self.i]


        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.i + 1 < len(self.l)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

