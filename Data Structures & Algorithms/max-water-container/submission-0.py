class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxVol = 0
        l = 0
        r = len(heights)-1

        while l < r:
            volume = (r-l) * min(heights[r], heights[l]) # calculate the volume
            maxVol = max(maxVol, volume) # save max volume
            if heights[l] <= heights[r]:
                l += 1
            elif heights[r] <= heights[l]:
                r-=1
        return maxVol
        