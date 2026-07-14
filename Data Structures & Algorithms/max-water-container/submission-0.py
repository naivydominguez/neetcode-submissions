class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        left, right = 0, len(heights)-1

        while left < right:

            if heights[left]< heights[right]:
                a = heights[left] * (right-left)
                maxAmount = max(maxAmount,a)
                left += 1
            
            elif heights[right] < heights[left]:
                a = heights[right] * (right-left)
                maxAmount = max(maxAmount,a)
                right -= 1 
            else:
                a = heights[left] * (right-left)
                maxAmount = max(maxAmount,a)
                left += 1
        
        return maxAmount


        