class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #if string contains all chars in another string, group them together
        #return all strings with similar string comps together
        res = {}

        #print(strs)
        for i in strs:
            key = "".join(sorted(i)) # this is our key to group anagrams
            if key in res:
                # when key is in our dict, append the word to a list, which
                # our dict will point to
                res[key].append(i)
            else: # create the list to append to
                res[key] = [i]
        
        result = list(res.values())

        return result