#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] 常数时间插入、删除和获取随机元素
#

# @lc code=start
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = set()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.l:
            return False
        self.l.add(val)
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.l:
            return False
        self.l.remove(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        a = list(self.l)
        index = random.randint(0, len(a)-1)
        return a[index]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

