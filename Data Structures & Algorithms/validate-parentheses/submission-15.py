class Solution:
    def isValid(self, s: str) -> bool:
        
        # conceptually, we push opening brackets on stack, and pop that value when we come across a
        # a relevant closing bracket
        # ex { -> } dict = { '}':'{' }
        # so :
        # 1. for each char in string
        # 2. check if is in our dict (check if its a pair)
        # 3. if its an opening bracket, append it to our stack
        # 3.5 if its a closing bracket AND it matches our opening bracket: POP IT, thus verifying that pair
        # 3.75 if it DOESNT match we must INSTANTLY FAIL, as it is not valid ex: ({)
        # 4. return true if stack is empty, false otherwise

        stack = []
        res = {'}':'{',')':'(',']':'['}
        #1
        for char in s:
            #2
            if char in res:
                #3.5
                if stack and stack[-1] == res[char]:
                    stack.pop()
                #3.75
                else:
                    return False
            #3
            else:
                stack.append(char)
        #4
        if stack:
            return False
        else:
            return True