class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s) - 1
        #s_ = s # fyi this is not a copy of the string, just another local var pointing at same string

        # if two cups need their liquids exchanged, you cant just pour one cup into the other.
        # we need a third cup to hold the value to be replaced.
        # this is where temp is used
        while left < right:
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

