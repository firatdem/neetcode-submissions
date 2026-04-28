class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window = []
        best = 0

        for char in s:
            # add the letters to our window, and drop when we get a repeat
            # its important to cut the problem letter from the first count
            # as well as readding it to the next count

            if char in window:
                if best < len(window):
                    best = len(window)
                indx = window.index(char)
                window = window[indx+1:]
                window.append(char)
            else:
                window.append(char)
            
            if best < len(window):
                best = len(window)
        return best