class Solution:
    def isValid(self, s: str) -> bool:
        
        # in valid parentheses all we have to do is
        # append opening parenths to a stack
        # we do this until we come across a closing parenth
        # now, a closing parenth means we must associate it with a corresponding
        # opening parenth.
        # so if invalid closing parenth, not associated with op, immeditate fail
        # if so, pop and consume the pair, and ensure stack is empty to return true
        # else return false, as all pairs not consumed

        res = {'}':'{',']':'[',')':'(',} # this is how we make the match
        stack = []

        for i in s:
            #print(i)
            if i in res:
                if stack and stack[-1] == res[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            

        # if stack not empty FAILLLLLL
        if stack:
            return False
        else:
            return True