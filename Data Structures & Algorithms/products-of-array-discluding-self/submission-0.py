class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            p=1
            parr=[]
            larr=[]
            pl=1

            for i in range(len(nums)):
                parr.append(p)
                p=p*nums[i]
                


            for j in range(len(nums)-1, -1,-1):
                larr.append(pl)
                pl=pl*nums[j]
                

            larr1 = larr[::-1]
            fi=1
            fiarr=[0] * len(nums)

            for i in range(len(nums)):
                fiarr[i]=larr1[i] * parr[i]
            
            return fiarr
        