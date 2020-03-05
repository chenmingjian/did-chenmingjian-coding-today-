#
# @lc app=leetcode.cn id=386 lang=python3
#
# [386] 字典序排数
#
from typing import *
# @lc code=start
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        a = list(range(1, n+1))
        a = sorted(list(map(str, a)))
        return list(map(int, a))

# @lc code=end

a = Solution().lexicalOrder(13)
print(a)