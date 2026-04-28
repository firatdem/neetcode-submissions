class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {} # track what we've seen so we dont need additional loops

        for i in range(len(nums)):
            needed = target - nums[i]
            print(needed)
            if needed in seen:
                return[seen[needed],i]
            else:
                seen[nums[i]] = i

        return []