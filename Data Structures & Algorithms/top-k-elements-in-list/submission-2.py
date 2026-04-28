class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #1. for each value in nums, we want to:
        #2. add them by key and value of count. counting occurences
        #3. once all added to dict, we must return the top k elements in the dict, by count

        result = []
        seen = {}
        # initialize entries in dict, creating entry if not found, and adding + 1 if found
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        
        for i in range(k):
            top = (max(seen, key=seen.get)) # THIS IS HOW WE RETURN THE TOP FROM SEEN
            result.append(top)
            seen[top] = 0 # 0 out the max so its nto counted again.

        return result
