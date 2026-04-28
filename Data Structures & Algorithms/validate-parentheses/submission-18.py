class Solution:
    def isValid(self, s: str) -> bool:
        
        # thie idea is to push opening parenths onto the stack
        # pop that corresponding open parenth when we  come across a close parenth
        # ye

        # first things first, set up our reference dict
        res = {'}':'{',')':'(',']':'['}
        stack = [] # non emtpy stack means we failed fyi

        for char in s:
            if char in res:
                if stack and stack[-1] == res[char]:
                    stack.pop()
                else: return False
            else:
                stack.append(char)            
        #print(stack)
        if stack:
            return False
        else:
            return True