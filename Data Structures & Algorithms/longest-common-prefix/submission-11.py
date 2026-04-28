class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # so, by index, we match character positions. if all char positions match
        # append he verified char to a result string, this is our return

        # for the loop, the base case will be our first string, and we must verify that strs
        # is non empty, and fail instantly if so.

        if not strs:
            return ""

        result = ""

        # set up base case
        first_word = strs[0]

        for i in range(len(first_word)):

            for word in strs:
                
                # Check if index is in the word we're CHECKING, not our base case.
                # and not equivalence, just less than
                if i < len(word) and word[i] == first_word[i]:
                    pass
                else:
                    return result
            result += first_word[i]

        return result