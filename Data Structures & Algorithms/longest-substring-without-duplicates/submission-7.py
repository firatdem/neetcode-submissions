class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 1. for each char in string
        # 2. record the string length upon each iteration, given there is no doubles, use stack here
        # 3. if character is a double, shrink the window ( window = window - index)
        # 3.5 we also have to record the length in another best value, can just be an int
        # 4. return largest sub string value

        best = 0
        window = []

        for char in s:
            # append each char to stack if not a repeat
            if char in window:
                indx = window.index(char) # this line gives us the index to slice with
                if best < len(window):
                    best = len(window)
                else:
                    pass
                # we must slice window, not reset
                window = window[indx+1:] # WE HAVE TO SLICE AT INDEX + 1 TO REMOVE OLD COPY OF CHAR
                window.append(char) # WE HAVE TO APPEND CHAR BACK TO CURRENT WORKING WINDOW
            else:
                window.append(char)
        if best < len(window):
            best = len(window)
        return best