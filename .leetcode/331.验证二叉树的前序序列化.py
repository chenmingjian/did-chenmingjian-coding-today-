#
# @lc app=leetcode.cn id=331 lang=python3
#
# [331] 验证二叉树的前序序列化
#

# @lc code=start
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = preorder.split(",")
        edges = 1
        for item in preorder:
            edges -= 1
            if edges < 0: return False
            if item != "#":
                edges += 2
        return edges == 0
# @lc code=end

