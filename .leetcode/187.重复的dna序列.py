#
# @lc app=leetcode.cn id=187 lang=python3
#
# [187] 重复的DNA序列
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        a = [s[i:i+10] for i in range(len(s) -9)]
        print(a)
        c = collections.Counter(a)
        
        ans = set()
        for k in c:
            if c[k] > 1:
                ans.add(k)

        return list(ans)
# @lc code=end
