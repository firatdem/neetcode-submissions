class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # 1. add values into dict
        # 2. check those values for each iteration
        # 3. if its the value we need yay

        seen = {}

        for i in range(len(nums)):

            needed = target - nums[i]

            if needed in seen:
                return[seen[needed],i]
            else:
                seen[nums[i]] = i
        return[]