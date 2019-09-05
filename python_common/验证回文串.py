from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.upper()
        new_s = "".join(list(filter(str.isalnum, s)))

        for i in range(int(len(new_s)/2)):
            if new_s[i] != new_s[-i-1]:
                return False

        return True


print(Solution().isPalindrome("0P"))
