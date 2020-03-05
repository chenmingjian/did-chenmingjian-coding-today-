#
# @lc app=leetcode.cn id=388 lang=python3
#
# [388] 文件的最长绝对路径
#

# @lc code=start
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        # print(input)
        d = {}
        a = input.split('\n')
         

        for i in a:
    
            if i[:1] != "\t":
                if '.' not in i:
                    d[i] = {}
                    this = []
                    this_level = 1
                    this.append(d[i])

                else:
                    d[i] = None
            else:
                level = len(i.split('\t'))-1
                print(i, level,     )
                while level < this_level:
                    this.pop()
                    this_level -= 1
                i = i.strip('\t')
                if level == this_level:                
                    if '.' in i:
                        this[-1][i] = None
                    else:
                        this[-1][i] = {}
                        this.append(this[-1][i])
                        this_level += 1

        all_list = []
        def ok(l,s=''):
            for i in l:
                if l[i] == None:
                    all_list.append(s+i)
                elif l[i] == {}:
                    pass
                else:
                    ok(l[i], s+i+'/')
        ok(d, '')
        print(all_list)
        print(d)
        return max(len(i) for i in all_list) if len(all_list) != 0 else 0
            


                    

# @lc code=end

a = Solution().lengthLongestPath("a\n\tb.txt\na2\n\tb2.txt")
print(a)