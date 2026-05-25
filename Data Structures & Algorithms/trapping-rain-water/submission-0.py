class Solution:
    def trap(self, height: List[int]) -> int:
            pre = []
            suf = []
            area = [0] * (len(height))
            f = 0

            for i in range(len(height)-1):
                b = i+1

                a = max(height[b:])
                suf.append(a)
            suf.append(0)
            pre.append(0)

            for i in range(len(height)-1):
                b = i+1
                a = max(height[:b])
                pre.append(a)


            for i in range(len(height)):
                area[i] = (min(pre[i], suf[i]) - height[i])
                if(area[i] > 0):
                    f+= area[i]
            return f
        