class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def multiplyByAll(arr):
            answer = []
            seen = {}
            for x in range(len(arr)):
                product = 1
                #print(arr[x])

                if arr[x] in seen:
                    answer.append(seen[arr[x]])
                    continue

                for y in range(len(arr)):
                    
                    if x == y:
                        pass

                    else:
                        product = product * arr[y]
                seen[arr[x]] = product
                answer.append(product)
            #print(seen)
            return answer

        ret = multiplyByAll(nums)
        return (ret)