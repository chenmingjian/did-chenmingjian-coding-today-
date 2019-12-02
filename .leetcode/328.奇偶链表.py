#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return
        if head.next == None:
            return head
        h = head
        i = 0
        ep = even_head = ListNode(float('inf'))
        op = odd_head = ListNode(float('inf'))
        epre = None
        opre = None
        while h:
            if i % 2 == 0:
                op.next = h
                opre = op 
                op = op.next
            else: 
                ep.next = h
                epre = ep
                ep = ep.next
            h = h.next
            i += 1
        print(even_head)
        print(odd_head)
        opre.next.next = even_head.next
        epre.next.next = None
        return odd_head.next
# @lc code=end

