class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        seen = {}

        for i in range(len(nums)):
            #print(nums[i])

            if nums[i] not in seen:
                seen[nums[i]] = 1
            else:
                seen[nums[i]] += 1
        max_key = (max(seen, key=seen.get))

        return max_key
