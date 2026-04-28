class Solution:
    def isValid(self, s: str) -> bool:
        
        res = {'}':'{',')':'(', ']':'['}
        stack = []

        # so the idea here is to use our dict to match our s[i]
        # to our opening bracket. append on open, pop on close
        # if stack empty, return true, else return false

        for ch in s: # for char in string
            if ch in res: # if character is in our dict.key section
                # if stack checks if empty
                # and if stack[-1] is the matching open parenthesis we need
                if stack and stack[-1] == res[ch]:
                    stack.pop() # if stack matches
                else:
                    return False # if not matching return false
            else: # if we get another open parenthesis
                stack.append(ch) # add the open parenthesis to the stack
            
        if not stack: # if stack empty return true
            return True
        else:
            return False