#
# @lc app=leetcode.cn id=373 lang=python3
#
# [373] 查找和最小的K对数字
#
from typing import *
# @lc code=start
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        streams = map(lambda u: ([u+v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]
# @lc code=end

Solution().kSmallestPairs([1, 7, 11], [2, 4, 6], 10)