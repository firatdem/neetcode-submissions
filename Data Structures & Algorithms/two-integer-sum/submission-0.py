class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        x = len(nums)

        for i in range(x):
            needed = target - nums[i]
            #print(needed)
            if needed in seen:
                return [seen[needed], i]
            seen[nums[i]] = i
        #print(seen)

        return []