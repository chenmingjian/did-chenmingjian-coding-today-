#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if head is None:
            return 

        h = head
        pre = None
        a = h
        while a:
            if pre is not None:
                pre.next = a 
            a.prev = pre
            if a.child is not None:
                child = self.flatten(a.child)
                a.next, a.child = child, a.next
                child.prev = a
                
                while child.next:
                    child = child.next
                child.next, a.child = a.child, None
                if child.next is None:
                    break
                child.next.prev = child
                a = child
            pre = a
            a = a.next
        return h

                
# @lc code=end

