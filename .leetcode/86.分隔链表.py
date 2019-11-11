#
# @lc app=leetcode.cn id=86 lang=python3
#
# [86] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        t = head 
        ans = []
        while t:
            ans.append(t.val)
            t = t.next

        a = []
        b = []
        for i in ans:
            if i < x:
                a.append(i)
            else:   
                b.append(i)

        ans = (a+b)[::-1]
        t = head
        while t:
            t.val = ans.pop()
            t = t.next

        return head
# @lc code=end

