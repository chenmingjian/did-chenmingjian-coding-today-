#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = []
        for s in strs:
            l = len(s)
            c = collections.Counter(s)

            for i in a:
                if i[0] == l:

                    for j in i[1]:
                        if c == j[0]:
                            j[1].append(s)
                            break
                    else:
                        i[1].append([c, [s]])

                    break
            else:
                a.append([l, [ [c, [s]] ]])

                
        print(a)
        return [ j[1] for i in a for j in i[1]]     
# @lc code=end

