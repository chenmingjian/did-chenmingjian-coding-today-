#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        h = ListNode(100)
        h.next = head

        c = 0
        t = h
        while c < m-1:
            t = t.next
            c += 1
        mt = t 
        while c < n:
            t = t.next
            c += 1
        nt = t

        print(mt.val, nt.val)
        p1 = mt.next
        mt.next = nt
        p2 = p1.next
        p1.next = nt.next

        while p1 != nt:
            if p2 is None:
                p0, p1=p1, p2
            else:
                p0, p1, p2 =p1, p2, p2.next 
            p1.next = p0
        
        return h.next
        
# @lc code=end

