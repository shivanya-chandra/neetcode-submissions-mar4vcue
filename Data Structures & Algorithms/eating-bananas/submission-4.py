class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        mini = max(piles)
        left = 1
        right = max(piles)
        # print(piles)

        while left <=right:
            mid = (left+right)//2
            hours = 0
            for i in range(len(piles)):
                if(piles[i] % mid == 0):
                    hours += piles[i] // mid
                else: 
                    hours += piles[i] // mid + 1
            # print(hours, "this is hours")

            if hours > h:
                left = mid + 1
                
            elif hours <= h:
                mini = min(mini, mid)
                # print(right, "this is right")
                # print(hours, "hrs")
                right = mid - 1
            # else:
            #     return mid
        return mini
        