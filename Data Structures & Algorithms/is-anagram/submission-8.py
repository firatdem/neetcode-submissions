class Solution:
    
    def isAnagram(self, s: str, t: str) -> bool:
        # Im thinking a dict approach will work here,
        # its just checking to see if both strings have
        # the same characters

        res = {}

        sorted_s = "".join(sorted(s)) # sorting strings is powerful, but you must break
        sorted_t = "".join(sorted(t)) # it down into chars, then join
        #print(sorted_s, sorted_t)
        if sorted_s == sorted_t:
            return True
        else:
            return False
        