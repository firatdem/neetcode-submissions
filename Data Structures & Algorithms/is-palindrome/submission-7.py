class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # building a string in python will require a nested loop, that would rebuild a string every iter.
        # this is obviously shitty, but its due to the immutable nature of strings in python

        # for an interview ready answer we need to be prepared to slve this using pointers

        # so the obvious thing tto do is add to a LIST and join chars at end
        
        # but above doesnt solve it the intended way, using pointers. so lets do that instead
        
        # the bottom line for the pointer solution is as follows
        # 1. set our pointers, and create a copy of our string to lower, or check as we loop, fuck that
        # 2. run the pointer manipulation while loop left < right
        # 3. we must check both ends to verify they are alphanumeric keys, one side increment if not
        # 3.5 important to note we must also recheck the while loop or we will get out of index errors
        # this is the and statements in our internal while loops
        # 4. once we verify, its a simple == check, if we fail this once, its not legal
        # 5 return true as it is implied if we dont return false from the internal else loop

        # 1
        left = 0
        right = len(s) - 1
        s_ = s.lower() # remove lowering from loop logic

        # 2
        while left < right:
            # 3 & 3.5
            # While loop til legal char for both ends
            while not s_[left].isalnum() and left < right:
                left += 1

            # 3 & 3.5
            while not s_[right].isalnum() and left < right:
                right -= 1
            # 4
            if s_[left] == s_[right]:
                pass
            else:
                return False

            # must increment at end since its a while, not a for
            left += 1
            right -= 1

        # 5
        return True
