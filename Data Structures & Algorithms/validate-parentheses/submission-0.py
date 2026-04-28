class Solution:
    def isValid(self, s: str) -> bool:
        
        res = {'}':'{',')':'(', ']':'['}
        stack = []

        # so the idea here is to use our dict to match our s[i]
        # to our opening bracket. append on open, push on close
        # if stack empty, return true, else return false

        for ch in s:
            if ch in res: # if character is in our dict.key section
                # if stack checks if empty
                # and if stack[-1] is the matching open parenthesis we need
                if stack and stack[-1] == res[ch]:
                    stack.pop()
                else:
                    return False # if not matching return false
            else: # if we get another open parenthesis
                stack.append(ch)
            
        if not stack:
            return True
        else:
            return False