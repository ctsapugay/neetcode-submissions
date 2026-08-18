class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        max_water = 0

        while l < r:
            volume = (r-l) * min(heights[l], heights[r])
            if max_water < volume:
                max_water = volume
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_water
            
        