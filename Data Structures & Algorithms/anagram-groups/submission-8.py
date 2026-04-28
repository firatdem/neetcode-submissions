class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # need a data struct to hold the results while maintainig index
        # HASH MAP HEHAHAHAH
        res = {}

        # put each word in a form that can be compared to other words
        for word in strs:
            sorted_word = "".join(sorted(word))

            # create a dict making our key the word, value is the sorted word
            if sorted_word in res:
                res[sorted_word].append(word)
            else:
                res[sorted_word] = [word]

            # sort into buckets based on dict association
        #print(res.values())
        return list(res.values())