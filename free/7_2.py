# by Bekzat
class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        check = False
        if x < 0: check = True
        x = abs(x)
        while x > 0:
            result += x % 10
            result *= 10
            x //= 10
        result //= 10
        if result < (-2) ** 31 or result > 2 ** 31 - 1:
            return 0
        if check: return("-" + str(result))
        return result

        
