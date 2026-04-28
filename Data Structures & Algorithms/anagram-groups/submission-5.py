class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # anagram is just same chars. we can simply sort them based on their keys

        res = {}

        for word in strs:
            key = ''.join(sorted(word))
            
            if key in res:
                res[key].append(word)
            else:
                res[key] = [word] # 

        result = res.values()
        result = list(result)

        return result
