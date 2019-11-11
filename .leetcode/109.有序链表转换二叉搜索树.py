#
# @lc app=leetcode.cn id=109 lang=python3
#
# [109] 有序链表转换二叉搜索树
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
    
        a = []

        while head:
            a.append(head.val)
            head = head.next

        print(a)
        def ok(l):
            if len(l) == 0:
                return None

            if len(l) == 1:
                return TreeNode(l[0]) 
            
            mid = len(l) // 2
            # print(l, mid)
            root = TreeNode(l[mid])

            l1 = l[:mid]
            # print(l1)
            root.left = ok(l1)

            l2 = l[mid+1 :]
            # print(l2)
            root.right = ok(l2)
            return root

        return ok(a)
            
        
# @lc code=end

