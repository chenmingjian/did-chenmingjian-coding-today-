#
# @lc app=leetcode.cn id=319 lang=python3
#
# [319] 灯泡开关
#
# https://leetcode-cn.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (43.58%)
# Likes:    70
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 14.3K
# Testcase Example:  '3'
#
# 初始时有 n 个灯泡关闭。 第 1 轮，你打开所有的灯泡。 第 2 轮，每两个灯泡你关闭一次。 第 3
# 轮，每三个灯泡切换一次开关（如果关闭则开启，如果开启则关闭）。第 i 轮，每 i 个灯泡切换一次开关。 对于第 n 轮，你只切换最后一个灯泡的开关。 找出
# n 轮后有多少个亮着的灯泡。
# 
# 示例:
# 
# 输入: 3
# 输出: 1 
# 解释: 
# 初始时, 灯泡状态 [关闭, 关闭, 关闭].
# 第一轮后, 灯泡状态 [开启, 开启, 开启].
# 第二轮后, 灯泡状态 [开启, 关闭, 开启].
# 第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 
# 
# 你应该返回 1，因为只有一个灯泡还亮着。
# 
# 
#
from typing import *
# @lc code=start
import math
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(math.sqrt(n))
# @lc code=end

tmp = Solution().bulbSwitch(3)
print(tmp)