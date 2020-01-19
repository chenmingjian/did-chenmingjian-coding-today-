#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
from typing import *
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        i = 0
        ij = 0
        j = 0
        ji = 0
        ans = []
        for _ in range(k):
            try:
                a = nums1[i] 
                b = nums2[ij]
                c = nums1[ji]
                d = nums2[j]
            except:
                break
            if a+b < c+d:
                ans.append(([a, b]))
                ij += 1
                if ij >= len(nums2):
                    ij = j+1
                    if ij >= len(nums2):
                        ij -= 1
                    i += 1
            else:
                ans.append([c, d])
                ji += 1
                if ji >= len(nums1):
                    ji = i+1
                    if ji >= len(nums1):
                        ji -= 1
                    j += 1
                    
        print(ans)
        return ans[1:]

# @lc code=end

Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 10)