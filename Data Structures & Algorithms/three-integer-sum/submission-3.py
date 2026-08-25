class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []

        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            
            left = i + 1
            right = len(sorted_nums) - 1

            while left < right:
                if left > right:
                    break
                temp = sorted([sorted_nums[i],sorted_nums[left],sorted_nums[right]])

                #print(temp)
                # make sure temp not in answer
                check = sum(temp)
                if check == 0 and temp not in answer:
                    answer.append(temp)

                if check < 0:
                    left += 1
                else:
                    right -= 1

        return answer