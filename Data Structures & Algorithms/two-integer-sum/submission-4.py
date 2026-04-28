class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hash map association so we get o(n)
        seen = {}

        for i in range(len(nums)):

            # use needed var to find if we've gone over a number that
            # is a potential fit
            needed = target - nums[i]
            #print(needed)
            if needed in seen:
                # to do check if our match is in dict, and return if so
                return[seen[needed],i]
            else:
                seen[nums[i]] = i

        return[]