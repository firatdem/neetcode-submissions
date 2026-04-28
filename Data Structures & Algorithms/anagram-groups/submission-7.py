class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagram is just same chars. we can simply sort them based on their keys

        # tips to employ the hash table here

        # 1. HOW DO WE ID? -> Sort by key, which is the word sorted. As we are anagram checking
        # 2. HOW DO WE SORT? -> Use a dict, and use our sorted word as a key, if the key doesnt exist
        # create a new sub list, if it does, modify the existing sublist.
        # 3. ONCE DICT HAS VALUES HOW THE HELL DO WE RETURN ANSWER? -> We use a list, we can convert
        # the values of our dict to a list using list(dict) , be careful not to use List.
        # also remember, dict.values() will return all values in a dict viewing format, not final.
        # To return it as a list, we must surround it in 'list(...)'

        res = {}

        for word in strs:
            key = ''.join(sorted(word))
            
            if key in res:
                res[key].append(word) # append to existing list by key
            else:
                res[key] = [word] # create the new list if doesnt exist

        result = res.values()
        result = list(result)

        return result
