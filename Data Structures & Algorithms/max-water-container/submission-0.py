class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights)-1
        max_water = 0

        while l < r:
            curr_width = r - l
            # get the height using the smaller height
            if heights[l] < heights[r]:
                # min height is of left side so we get the heigh
                height = heights[l]*curr_width
                l += 1
            elif heights[r] < heights[l]:
                height = heights[r] * curr_width
                r -= 1
            else:
                # same height
                height = heights[r] * curr_width
                l +=1
                r -=1

            max_water = max(height, max_water)

        return max_water            


