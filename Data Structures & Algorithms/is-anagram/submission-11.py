class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        # use this to increment count, decrement when checking
        alphabet = "abcdefghijklmnopqrstuvwxyz"

        counts = [0] * len(alphabet)

        # use position as the index checker, prints a number when
        # using alphabet.index
        for char in s:
            position = alphabet.index(char)
            counts[position] += 1
        
        for char in t:
            position = alphabet.index(char)
            counts[position] -= 1

        for each in counts:
            #print(each)
            if each > 0:
                return False
            
        return True