#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        one = ListNode(0)

        tmp = one 
        p = head
        while p:
            q = one
            while q.next is not None and p.val > q.next.val:
                q = q.next
            tmp = p.next
            p.next, q.next = q.next, p
            p = tmp

        return one.next
# @lc code=end

