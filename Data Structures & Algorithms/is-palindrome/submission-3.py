class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # so when we reverse, those built in features dont accoutn for special chars
        # so if we do a for loop, how do we ensure we skip problems, and make sure everything is lower
        
        reverse_s = ''
        not_allowed = [' ', '?', '!', '.', ',', '`',"'",':',';'] 
        s_ = ''

        for char in range(len(s)-1,-1,-1):
            if s[char] in not_allowed:
                pass
            else:
                reverse_s += s[char].lower()
        for char in range(len(s)):
            if s[char] in not_allowed:
                pass
            else:
                s_ += s[char].lower()
        print('reversed', reverse_s)
        print('converted', s_)

        if s_ == reverse_s:
            return True
        else:
            return False