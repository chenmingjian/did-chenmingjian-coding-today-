from typing import *
import collections

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        d = {}
        d2 = {}
        for i in regions:
            # print(i)
            d[i[0]] = {j:{} for j in i[1:]}
        del_index = []
        
        for i in d:
            for j in d:
                if i in d[j]:
                    d[j][i] = d[i]
                    
                    del_index.append(i)
        for i in del_index:
            d.pop(i)
        
        
        deque = collections.deque([(i, d[i], None) for i in d])
      
        while deque:
            k, a, father = deque.popleft()
            
            if father is None:
                d2[k] = [k]
            else:
                d2[k] = d2[father] + [k]
            if region1 in d2 and region2 in d2:
                break    
            for i in a:
                deque.append((i,a[i], k))

        ans = ''
        for i, j in zip(d2[region1], d2[region2]):
            if i == j:
                ans = i
            else:
                break