#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        if len(s) > 12:
            return []
        for i in itertools.combinations(range(1, len(s)), 3):
            a = [s[0:i[0]], s[i[0]:i[1]], s[i[1]:i[2]], s[i[2]:]]
            for i in a:
                if int(i) > 255:
                    break
                if len(i) > 1 and i[0] == '0':
                    break
            else:
                tmp = ''.join([i + '.' for i in a])[:-1]
                print(tmp)
                ans.append(tmp)
                # ans.append(s[0:i[0]] + '.' + s[i[0]:i[1]] + '.' + s[i[1]:i[2]] + '.' + s[i[2]:])

        return ans
# @lc code=end

