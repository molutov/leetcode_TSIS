# by Bekzat
class Solution:
    def reverse(self, x: int) -> int:
        if x == 0: return 0
        check = False
        if x < 0:
            check = True
            x *= -1
        s = str(x)
        s = s[::-1]
        if int(s) < (-2) ** 31 or int(s) > 2 ** 31 - 1: return 0
        for i in range(len(s)):
            if s[i] != "0":
                if check: return("-" + s[i::])
                else: return(s[i::])
