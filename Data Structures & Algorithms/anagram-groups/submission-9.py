class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs) == 0:
            return[""]

        # make buckets for each
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        seen = {}

        result = []

        for word in strs:
            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word in seen:
                seen[sorted_word].append(word)
            else:
                seen[sorted_word] = [word]
        print (seen.values())
        return (list(seen.values()))

        