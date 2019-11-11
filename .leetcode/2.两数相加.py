#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def list2num(l):
            a = []
            while l:
                if l == None:
                    break
                a.append(l.val)
                l = l.next
            s = ''.join([str(i) for i in a[::-1]])
            return int(s)

        b1 = list2num(l1)
        b2 = list2num(l2)
        
        ans = b1 + b2

        def num2list(n):
            l = None
            for c in str(n):
                if l is None:
                    l = ListNode(int(c))
                else:
                    tmp = l
                    l = ListNode(int(c))
                    l.next = tmp
            return l
        
        return num2list(ans)
        
# @lc code=end

