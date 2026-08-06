class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}
        highest = []

        for num in range(len(nums)):

            if nums[num] in seen:
                seen[nums[num]] += 1
                # Believe we could nest our top number checker here.
                # Separate for simplicity
            else:
                seen[nums[num]] = 1

        #print(seen)
        # now we just have to compare keys based on their values

        for key in sorted(seen, key = seen.get, reverse=True):
            if len(highest) == k:
                return highest
            else:
                highest.append(key)

        return highest