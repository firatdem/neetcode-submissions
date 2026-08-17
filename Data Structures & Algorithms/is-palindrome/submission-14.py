class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s) - 1

        while left < right:
            # skip invalid characters on left
            while not s[left].isalnum() and left < right:
                left += 1
            # skip invalid characters on right
            while not s[right].isalnum() and left < right:
                right -= 1
                
            # compare s[left] and s[right]
            if s[left].lower() == s[right].lower():
                pass
            else:
                return False
            # move both inward
            left += 1
            right -= 1
        
        return True