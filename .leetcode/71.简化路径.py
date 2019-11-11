#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:

        a = path.split('/')
        ans = []
        for i in a:
            if i == '.' or i == "":
                continue
            elif i == '..':
                ans.pop() if len(ans) > 0 else None
            else:
                ans.append(i)

        return '/' + ''.join([i+'/' for i in ans])[:-1]
        
# @lc code=end

