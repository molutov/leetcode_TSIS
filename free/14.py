# by Bekzat
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        k = min(strs)
        for i in range(len(k), 0, -1):
            check = True
            for j in strs:
                if j[:i] != k[:i]:
                    check = False
            if check:
                return k[:i]
        return ""
