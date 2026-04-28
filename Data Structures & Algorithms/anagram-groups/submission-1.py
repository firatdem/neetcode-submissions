class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {} # For key association

        for i in strs:
            # Create the key based on sorting the strings
            # This associates all words with the same chars
            # think of it as x.y(z); makes it easier to remember
            # z is placing our string into the sorted function
            # y is joining the chars of the sorted function
            # x is our 'to string' function
            key = "".join(sorted(i))
            
            # Check if key is new, and if it isnt, add it to existing group
            # based on key association in our dict -> 'res'
            if key not in res:
                res[key] = []
            res[key].append(i)

        #print(res)
        # This converts the VALUES of our dict to a list, as the expected output is list
        result = list(res.values())
        
        return result
        