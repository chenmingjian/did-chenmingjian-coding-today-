#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        a = [i for i in arr1 if i in arr2]
        b = [i for i in arr1 if i not in arr2]
        b.sort()
        a.sort(key= lambda x: arr2.index(x))
        return a + b
# @lc code=end

