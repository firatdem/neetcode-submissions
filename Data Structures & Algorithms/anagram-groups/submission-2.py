class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sorted_list = [] # hold string signatures
        signatures = {}
        result = []

        for i in range(len(strs)):
            
            sorted_s = "".join(sorted(strs[i]))
            sorted_list.append(sorted_s)
            # if our seen is present in the dict
            # append to a list
            # if not create a new list
            # associate with dict by creating a list in case not found in seen dict
            # using our sorted_s as our key
            if sorted_s in signatures:
                #print('append to existing list')
                signatures[sorted_s].append(strs[i])

            else:
                #print('create new list to append to')
                # in case it hasnt been seen
                signatures[sorted_s] = [strs[i]]

        for i in signatures:
            result = list(signatures.values())
            #result += a
        #print(signatures)

        return result