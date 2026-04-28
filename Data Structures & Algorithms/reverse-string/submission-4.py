class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s) - 1

        # to reverse, we have to swap places, based on a shrinking window
        # only do this while left < right otherwise, we begin to overwrite overwritten data

        while left < right:

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1