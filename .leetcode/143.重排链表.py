#
# @lc app=leetcode.cn id=143 lang=python3
#
# [143] 重排链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        a = []
        while head:
            a.append(head)
            head = head.next
        
        i = 0
        j = len(a) - 1
        h = ListNode(9999)
        while i <= j:

            if i == j:
                h.next = a[i] 
                h = h.next
                break
            h.next = a[i] 
            h.next.next = a[j]
            h = h.next.next

            i += 1
            j -= 1

        h.next = None
        return a[0]
# @lc code=end

