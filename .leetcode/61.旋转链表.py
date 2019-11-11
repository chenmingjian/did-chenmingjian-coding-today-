#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import *
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        a = []
        while head:
            a.append(head)
            head = head.next
        if len(a) <= 0:
            return head
        k = k % len(a)
        if k == 0:
            return a[0]
        a[-k-1].next = None
        head = a[-k]
        a[-1].next = a[0]
        return head
# @lc code=end

print(Solution().rotateRight([0]))
