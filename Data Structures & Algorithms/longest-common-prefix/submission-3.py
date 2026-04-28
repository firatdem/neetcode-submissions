class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        result = ""

        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            for word in strs: # fail if word too short or chras differ
                if i >= len(word) or word[i] != char:
                    return result

            result += char

        return result