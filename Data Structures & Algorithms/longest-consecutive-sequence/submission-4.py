class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        longest = 1
        temp = 0
        sor = sorted(nums)

        for i in range(len(sor)):

            if i + 1 >= len(sor):
                if temp + 1 > longest:
                    longest = temp + 1
                break

            elif sor[i] + 1 == sor[i + 1]:
                # consecutive number found
                temp += 1

            elif sor[i] == sor[i + 1]:
                # duplicate, ignore it
                continue

            else:
                # sequence broke
                if temp + 1 > longest:
                    longest = temp + 1

                temp = 0

        return longest