class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # the tricky part is traversing down the side of the list
        # and not through each word

        if not strs:
            return ""
        
        result = ""

        first_word = strs[0]

        for i in range(len(first_word)):
            char = first_word[i]

            for word in strs: # fail if word too short or chars differ
                if i >= len(word) or word[i] != char:
                    return result

            result += char
        
        return result
