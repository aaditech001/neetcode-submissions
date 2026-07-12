class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        maximum_area=0
        while l<r:
            water_contain=(r-l)*min(heights[r], heights[l])
            maximum_area= max(maximum_area,water_contain)
            if heights[r]>heights[l]:

                l+=1
            else:
                r-=1
        return maximum_area
        