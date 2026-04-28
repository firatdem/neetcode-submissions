class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # check for empty list
        if not strs:
            return ""

        # return at the end
        result = ""

        # if str empty, fail before we get here
        first_word = strs[0]

        for i in range(len(first_word)):

            # check along the first word
            for word in strs:
                # skip first word
                if i < len(word) and word[i] == first_word[i]:
                    pass
                else:
                    return result
            result += first_word[i]

        return result