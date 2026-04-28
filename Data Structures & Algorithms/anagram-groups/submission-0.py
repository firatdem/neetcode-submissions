class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # map charCount to list of anagrams
        sorted_list = []

        # try to brute force first
        x = (len(strs))

        for i in range(x):
            s = strs[i]
            sorted_s = "".join(sorted(s)) # This line takes a string s and sorts it
                                          # Returning the sorted version of it
            sorted_list.append(sorted_s)

        # I do not quite grasp this loop yet
        for i in range(len(strs)):
            key = sorted_list[i]
            res.setdefault(key, []).append(strs[i])

        return list(res.values())
