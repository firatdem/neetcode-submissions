class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for num in range(len(nums)):

            #print(num) INDEX
            #print(nums[num]) ACTUAL VALUE
            # DUE TO USE USING THE RANGE OF THE NUMS ARRAY

            needed = target - nums[num]

            if needed in seen:
                return[seen[needed], num]
            else:
                seen[nums[num]] = num

