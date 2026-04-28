class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1 # due to array offset
        s_ = s.lower() # just save on cleaning up in the loop

        while left < right:
            #print(s_[left],s_[right])
            while not s_[left].isalnum() and left < right: # when our value is not alphanumeric, its cool
                left += 1 # skip that value

            while not s_[right].isalnum() and left < right: # when our value is not alphanumeric, its cool
                right -= 1 # skip that value
            
            # if the characters, not considering space or other spec character
            # do not match, fail immediately, as we dont have to check shit else
            if s_[left] == s_[right]:
                pass
            else:
                return False
            
            left += 1
            right -= 1

        # if no falses, assumed to be true
        return True