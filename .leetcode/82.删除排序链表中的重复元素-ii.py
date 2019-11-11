#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        d = collections.OrderedDict()

        while head:
            if head.val in d:
                d[head.val] += 1
            else:
                d[head.val] = 1
            head = head.next
        print(d)

        e = [k for k in d.keys() if d[k] <= 1]
        if len(e) == 0:
            return
        head = ListNode(e[0])
        p = head
        for i in e[1:]:
            p.next = ListNode(i)
            p = p.next
        return head
            
# @lc code=end

