class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        new_list = []
        for num in nums:
            new_list.append(num)
        result = nums + new_list
        return result
