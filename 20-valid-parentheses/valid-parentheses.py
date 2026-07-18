class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []
        valid = {"}":"{",
                 ")":"(",
                 "]":"["}

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if stack == []:
                    return False
                else:
                    if valid[ch] == stack[-1]:
                        stack.pop()
                    else:
                        return False

        
        return stack == []
