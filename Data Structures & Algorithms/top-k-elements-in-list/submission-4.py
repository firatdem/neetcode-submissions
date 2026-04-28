class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        i = 0 # for the final pop loop

        for num in nums:
            # Todo: put our nums in a dict, values will be the count
            if num in freq:
                freq[num] += 1 # increment the count
            else:
                freq[num] = 1 # init the count

        # use this to sort the list using our return from freq, ie the count
        sorted_nums = sorted(freq, key=freq.get, reverse=True)
        # pop off the lowest, since were sorted, while length over k
        while len(sorted_nums) > k:
            sorted_nums.pop()

        return sorted_nums