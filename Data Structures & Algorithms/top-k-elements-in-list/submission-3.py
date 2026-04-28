class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        result = []

        for i in range(len(nums)):

            if nums[i] in freq:
                freq[nums[i]] += 1 # add to count
            else:
                freq[nums[i]] = 1  # initialize if not in dict

        
        result = sorted(freq,key=freq.get, reverse=True) # this line is sick, reverse sort by key=freq.get
        i = len(result)
        #print(i,k)
        while i > k:
            result.pop()

            i -= 1
        return result