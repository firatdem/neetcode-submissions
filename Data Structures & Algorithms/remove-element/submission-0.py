class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Never mutate a list while iterating forward over its indices.
        # will always be out of index

        for i in range(len(nums) - 1, -1, -1): # range has 3 hidden attributes
                                               # range( start , stop , step )
                                               # we use this to go backwards
                                               # and never go out of index
            if nums[i] != val:
                pass
            else:
                nums.pop(i)
        result = len(nums)
        return result