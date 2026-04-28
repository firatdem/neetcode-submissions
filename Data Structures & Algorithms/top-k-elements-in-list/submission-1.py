class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {} # using this to keep num as key and count as value
        result = [] # use this to append our tops to

        for i in nums:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        #print(count.values())

        for i in range(k):
            result.append(max(count, key=count.get)) # -> important, print key based
                                                     # on max value, crucial for top k
            count[max(count, key=count.get)] = 0
        print(result)

        return result