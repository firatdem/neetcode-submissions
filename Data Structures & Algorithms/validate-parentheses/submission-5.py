class Solution:
    def isValid(self, s: str) -> bool:
        
        keys = {'}':'{',')':'(',']':'['}
        stack = []

        # for each character in string s
        for ch in s:
            # if character corresponds to a key in our dict
            if ch in keys:

                # If stack is non empty AND top of stack matches key of character
                # pop that element from stack
                # i.e. the corresponding closing bracket
                if stack and stack[-1] == keys[ch]:
                    stack.pop()
                else:
                    return False # fail on first mismatch
            # append to stack, first step into loop essentially
            else:
                stack.append(ch)

                
        if stack:
            return False
        else:
            return True