class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # so basically in a LCP problem
        # we check along the END of the words
        # We use word 1 as our base case, which hung me up the first time I attempted
        # then FOR INDEX RANGE in word 1, we again check EACH WORD IN STRS,
        # we check letters by INDEX

        #fail if list is empty
        if not strs:
            return ""

        # result to return
        result = ""

        # set base case
        first_word = strs[0]

        # check the first word because whole case fails if first doesnt work!
        for i in range(len(first_word)):
            for word in strs:
            # if the whole range of letters in index i match first_word
            # append it to our result, but only AFTER comfirmed against whole list
            
            # using a nested for loop to toggle through EACH word
            # after setting up the index selection
            # got a little mixed up.
                if i < len(word) and first_word[i] == word[i]:
                    pass
                else:
                    return result
            # append only after each WORD!!
            result += first_word[i]
        return result