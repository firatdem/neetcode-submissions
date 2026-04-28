class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # the big thing to remember here is when we cut the current longest string,
        # we have to remove the problem character from the LAST string,
        # then ADD it to our new string, or we will have mismatched string lengths 

        # lets not be afraid to do this in 3 parts. and lets avoid the max(), fall back if necessary

        #1. lets add our string to a list, we dont need a dict
        window = []
        best = 0 # -> hold our largest string length
        for char in s:
            # if our character is in window, we must remove all instances left of our index
            # then RE ADD our index to the new count
            if char in window:
                if best < len(window):
                    best = len(window)
                # resetting window is NOT the right move, we have to slice it, how do we do that...
                index = window.index(char)
                window = window[index+1:]
                window.append(char) # WE MUST APPEND IT BACK TO LIST
            else:
                window.append(char)
                #print(window)

        # also need a final comparison, because we neglect our own logic if not
        if best < len(window):
            best = len(window)
        return best