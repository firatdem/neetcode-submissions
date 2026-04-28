class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean = ''
        left = 0
        right = len(s) -1

        for char in s:

            if char.isalnum():
                clean += char.lower()
            else:
                pass
        
        reversed_s = clean[::-1] # simple way to reverse a cleaned string
        #print(reversed_s)

        if clean == reversed_s:
            return True
        else:
            return False