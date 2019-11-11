#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        a = [i for i in range(len(arr)) if arr[i] == 0]

        for i, j in enumerate(a):
            arr.insert(j+i, 0)
        for _ in range(len(a)):
            arr.pop()
            
        
# @lc code=end

