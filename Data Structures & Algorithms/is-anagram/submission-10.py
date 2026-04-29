class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # technically i can just make an array of 26 0's and use it as a code for alphabet.
        # add for first word, subtract for second, thus, if unequla balance, false

        if len(s) != len(t):
            return False

        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        print(s_sorted)
        print(t_sorted)

        for char in range(len(s_sorted)):
            if s_sorted[char] == t_sorted[char]:
                continue
            else:
                return False

        return True