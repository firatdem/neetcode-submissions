class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def getWidth(l,r):
            return(r-l)

        def getHeight(m1,m2):
            return min(m1,m2)

        largest = 0

        left = 0
        right = len(heights) - 1

        while left < right:

            # 1. compare taller height
            # 1.2 if left taller, move right inward
            # 1.3 if right taller, move left inward

            w = getWidth(left,right)
            h = getHeight(heights[left],heights[right])

            a = h * w

            if largest < a:
                largest = a

            # pointer moving logic herrrr
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return largest