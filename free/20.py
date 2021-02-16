# by Bekzat
class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        check = ["(", "[", "{"]
        for x in s:
            if len(l) == 0:
                l.append(x)
            else:
                top = l[len(l) - 1]
                if top in check and x in check:
                    l.append(x)
                elif (top == "(" and x == ")") or (top == "[" and x == "]") or (top == "{" and x == "}"):
                    l.pop()
                else:
                    l.append(x)
        if len(l) == 0:
            return True
        else:
            return False
        
