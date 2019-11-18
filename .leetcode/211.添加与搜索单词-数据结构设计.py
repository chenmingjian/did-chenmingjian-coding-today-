#
# @lc app=leetcode.cn id=211 lang=python3
#
# [211] 添加与搜索单词 - 数据结构设计
#

# @lc code=start
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        d = self.d
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['isEnd'] = None
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        d = self.d
        pre = ''
        for index, i in enumerate(word):
            
            if i == '.':
                return any(map(self.search, [pre+i+word[index+1:] for i in d]))
            pre += i
            if i not in d:
                return False
            d = d[i]
        
        return 'isEnd' in d

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

