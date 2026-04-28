class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # so the idea is probably to make a copy of string
        # that will be lowered, and have spaces removed

        # checking palindrome so that means left = right
        # could use a window again

        left = 0
        right = len(s) - 1

        # make a copy of string to make the lower checks easier
        s_ = s.lower()

        while left < right:
            
            # these have to be while loops!!!!
            # check if loop still valid, and if s_left alphanumeric
            while not s_[left].isalnum() and left < right:
                left += 1 # push pointer past

            while not s_[right].isalnum() and left < right:
                right -= 1 # push pointer past

            print(s_[left], s_[right])
            if s_[left] != s_[right]:
                return False
            
            left += 1
            right -= 1

        return True
                