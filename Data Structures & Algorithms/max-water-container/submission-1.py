class Solution:
    def maxArea(self, heights: List[int]) -> int:
            j = 0
            k = len(heights) - 1
            maxi = 0
            for i in range(len(heights)):

                x = min(heights[j], heights[k])
                area = x * (k-j)
        


                maxi = max(area, maxi)

                

                if(heights[j] < heights[k]):
                    j += 1

                else:
                    k-=1
            return(maxi)
        