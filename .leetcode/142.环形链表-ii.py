#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        a = {}
        c = 0
        while head:
            if head not in a:
                a[head] = c
            else:
                return a[head]
            c += 1
            head = head.next
# @lc code=end

