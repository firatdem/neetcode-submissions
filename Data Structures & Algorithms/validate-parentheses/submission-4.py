class Solution:
    def isValid(self, s: str) -> bool:
        
        keys = {'}':'{',')':'(',']':'['}
        stack = []

        for ch in s:
            if ch in keys:

                # If stack is non empty AND top of stack matches 
                # i.e. the corresponding closing bracket
                if stack and stack[-1] == keys[ch]:
                    stack.pop()
                else:
                    return False # fail on first mismatch
            else:
                stack.append(ch)

                
        if stack:
            return False
        else:
            return True