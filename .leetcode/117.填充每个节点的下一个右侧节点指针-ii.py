#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = collections.deque()
        q.append((root, 0))

        pre = None
        while q:
            n, l = q.popleft()

            if n is not None:
                if pre is None:
                    pre = n, l
                else:
                    if l == pre[1]:
                        pre[0].next = n
                    pre = n, l
                q.append((n.left, l+1))
                q.append((n.right, l+1))

        return root
# @lc code=end

