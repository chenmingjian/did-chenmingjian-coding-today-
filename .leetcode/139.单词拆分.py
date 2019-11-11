#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#
from typing import *
# @lc code=start
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        d = {}
        a = set()
        b = set()
        for i in wordDict:
            if i[0] not in d:
                d[i[0]] = [i]
            else:
                d[i[0]].append(i)
        def ok(ss):
            if len(ss) == 0:
                return True
            if ss[0] not in d:
                return False

            ans = []
            for i in d[ss[0]]:
                l = len(i)
                if i == ss[:len(i)]:
                    if ss[l:] not in a and ss[l:] not in b:
                        tmp = ok(ss[l:])
                        if tmp is False:
                            b.add(ss[l:])
                        else:
                            a.add(ss[l:])

                    else:
                        tmp = True if ss[l:] in a else False
                            

                    ans.append(tmp)

            return any(ans)

        return ok(s)


# @lc code=end

print(Solution().wordBreak("acaaaaabbbdbcccdcdaadcdccacbcccabbbbcdaaaaaadb", ["abbcbda","cbdaaa","b","dadaaad","dccbbbc","dccadd","ccbdbc","bbca","bacbcdd","a","bacb","cbc","adc","c","cbdbcad","cdbab","db","abbcdbd","bcb","bbdab","aa","bcadb","bacbcb","ca","dbdabdb","ccd","acbb","bdc","acbccd","d","cccdcda","dcbd","cbccacd","ac","cca","aaddc","dccac","ccdc","bbbbcda","ba","adbcadb","dca","abd","bdbb","ddadbad","badb","ab","aaaaa","acba","abbb"]))