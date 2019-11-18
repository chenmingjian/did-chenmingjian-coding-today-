#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        d = self.d
        for i in word:
            if i not in d:
                d[i] = {}
            d = d[i]
        d['isEnd'] = None  

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        d = self.d
        for i in word:
            if i in d:
                d = d[i]
            else:
                break
        else:
            return 'isEnd' in d
        return False
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        d = self.d
        for i in prefix:
            if i in d:
                d = d[i]
            else:
                return []

        ans = []

        def getStr(dd, head):
            if 'isEnd' in dd:
                ans.append(head)
                return
            for i in dd:
                getStr(dd[i], head+i)

        getStr(d, prefix)
        return ans
            

        



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

