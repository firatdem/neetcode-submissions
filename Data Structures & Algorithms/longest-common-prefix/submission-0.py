class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # so conceptually, i have to check the first character of each string
        # the minute one doesnt match, we faill

        # doint underestimate the base case

        if not strs:
            return ""

        prefix = ""

        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            for word in strs:
                # fail if word is too short or chars differ
                if i >= len(word) or word[i] != char:
                    return prefix

            prefix += char

        return prefix