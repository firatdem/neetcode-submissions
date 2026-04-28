class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""
        
        result = ""

        first_word = strs[0]

        # check length of first word
        for i in range(len(first_word)):

            for word in strs:
                if i < len(word) and word[i] == first_word[i]:
                    pass
                else:
                    return result
            result += first_word[i]

            # check if i is within range, if so, check if characters match first word
            # based on index in our loop
        return result