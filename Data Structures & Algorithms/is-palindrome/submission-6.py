class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # building a string in python will require a nested loop, that would rebuild a string every iter.
        # this is obviously shitty, but its due to the immutable nature of strings in python

        # for an interview ready answer we need to be prepared to slve this using pointers

        # so the obvious thing tto do is add to a LIST and join chars at end
        
        # but above doesnt solve it the intended way, using pointers. so lets do that instead
        left = 0
        right = len(s) - 1
        s_ = s.lower() # remove lowering from loop logic

        while left < right:
            # While loop til legal char for both ends
            while not s_[left].isalnum() and left < right:
                left += 1

            while not s_[right].isalnum() and left < right:
                right -= 1
            # compare once sure they r legal
            if s_[left] == s_[right]:
                pass
            else:
                return False

            left += 1
            right -= 1

        return True
