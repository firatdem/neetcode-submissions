class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_ = sorted(s)
        t_ = sorted(t)

        if s_ == t_:
            return True
        else:
            return False