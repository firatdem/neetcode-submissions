class Solution:
    def isValid(self, s: str) -> bool:
        
        # thie idea is to push opening parenths onto the stack
        # pop that corresponding open parenth when we  come across a close parenth
        # ye

        # first things first, set up our reference dict
        res = {'}':'{',')':'(',']':'['}
        stack = [] # non emtpy stack means we failed fyi

        # important mental model to note
        # the nested if is easier to conceptualize when you make a broad first if, and break it down
        # for example i started with if char in res AND stack[-1] == res[char], thus it was trying
        # to check if the char matched the stack and was in dict, obviously impossible
        # approach things broadly and fine tune the approach using prints
        for char in s:
            # is our char a closing bracket?
            if char in res:
                # is our stack non empty AND does the value (ie the closing parenth)
                # match the top (opening parenth) of our stack?
                # if so pop and consume, thus verifying that pair
                if stack and stack[-1] == res[char]:
                    stack.pop()
                # this is important because if the parenth is closing but does not match the opening, we fail
                else:
                    return False
            # keep it moving in case of opening brackets
            else:
                stack.append(char)
        #print(stack)
        if stack:
            return False
        else:
            return True