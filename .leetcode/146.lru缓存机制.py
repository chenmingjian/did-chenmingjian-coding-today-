#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
import collections
# @lc code=start
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.d = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        self.d.move_to_end(key)
        # print(self.d)
        return self.d[key]

    def put(self, key: int, value: int) -> None:
        self.d[key] = value
        self.d.move_to_end(key)
        
        if len(self.d) > self.cap:
            self.d.popitem(False)
        # print(self.d)
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

