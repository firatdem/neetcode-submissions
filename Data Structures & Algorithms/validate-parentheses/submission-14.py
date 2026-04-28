class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        res = {'}':'{',']':'[',')':'('}

        # push onto stack if opening bracket
        for char in s:
            #print(res[char])

            # 1. check if char is in dict
            if char in res:
                # if stack is non empty and our char is a parenth pair, consume and verify
                if stack and stack[-1] == res[char]:
                    stack.pop()
                # if the char is not a valid pair, fail instantly.
                else:
                    return False
            # append when its not a closing parenth to be paired
            else:
                stack.append(char)
        # return true for empty stack, thus meaning everything consumed
        if stack:
            return False
        else:
            return True