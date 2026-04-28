class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        res = {'}':'{',']':'[',')':'('}

        # push onto stack if opening bracket
        for char in s:
            #print(res[char])
            # if our character is an opening bracket, push it onto stack
            if char in res: # if char is closing bracket, consume our open bracket
                                                       # in our stack, thus verifying pair
                if stack and stack[-1] == res[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if stack:
            return False
        else:
            return True