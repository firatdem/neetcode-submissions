class Solution:
    def isValid(self, s: str) -> bool:
        
        # when we see an opening parenth, append to stack
        # when we see relevant closing parenth pop that corresponding op bracket
        # this consumes and verifies that pair
        # IF WE SEE A NON RELEVANT CLOSE PARENTH FAIL IMMEDIATELY!!!
        # if another opening parenth, simply append again, cuz that breaks no rules

        stack = []
        res = {'}':'{',')':'(',']':'['}

        for char in s:

            if char in res and stack:
                if stack[-1] == res[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)


        if stack:
            return False
        else:
            return True