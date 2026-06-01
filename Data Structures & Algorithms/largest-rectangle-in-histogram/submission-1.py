class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ar = 0
        for i in range(len(heights)):
            idi = i
            while st and st[-1][1] > heights[i]:
                idi = st[-1][0]
                a = st.pop()
                ar = max(ar, a[1] * (i - a[0]))    
            st.append([idi, heights[i]])
        for i in range(len(st)):
            ar = max(ar, st[i][1] * (len(heights) - st[i][0]))

        return ar
        