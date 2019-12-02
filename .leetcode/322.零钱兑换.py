#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#
# https://leetcode-cn.com/problems/coin-change/description/
#
# algorithms
# Medium (36.40%)
# Likes:    286
# Dislikes: 0
# Total Accepted:    30.7K
# Total Submissions: 84.4K
# Testcase Example:  '[1,2,5]\n11'
#
# 给定不同面额的硬币 coins 和一个总金额
# amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
# 
# 示例 1:
# 
# 输入: coins = [1, 2, 5], amount = 11
# 输出: 3 
# 解释: 11 = 5 + 5 + 1
# 
# 示例 2:
# 
# 输入: coins = [2], amount = 3
# 输出: -1
# 
# 说明:
# 你可以认为每种硬币的数量是无限的。
# 
#
from typing import *
# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}
        def ok(_amount):
            if _amount == 0:
                return 0
            if _amount in coins:
                return 1
            if _amount in dp:
                return dp[_amount]
            all_situation = []
            for i in coins:
                if _amount >= i:
                    left = _amount - i
                    if left not in dp:
                        dp[left] = ok(left)
                    if dp[left] == -1:
                        continue
                    all_situation.append(dp[left] + 1)
            if len(all_situation) == 0:
                return -1
            return min(all_situation)
 
        tmp = ok(amount)
        print(dp)
        return tmp


# @lc code=end

tmp = Solution().coinChange([2], 3)
print(tmp)