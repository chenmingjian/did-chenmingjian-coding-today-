from typing import *


def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a


print(singleNumber([2, 2, 1]))
