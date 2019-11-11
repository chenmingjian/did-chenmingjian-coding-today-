#
# @lc app=leetcode.cn id=89 lang=python3
#
# [89] 格雷编码
#

# @lc code=start
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        s = "0" * n
        ans = [s]
        while True:
            for i in range(len(s)):
                if s[i] == '0':
                    new = s[:i] + '1' + s[i+1:]
                else:
                    new = s[:i] + '0' + s[i+1:]
                print(s, new)
                
                if new not in ans:
                    ans.append(new)
                    s = new
                    break
            else:
                break
        print(ans)
        return [int(i, 2) for i in ans]
                

# @lc code=end

