class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        
        h=[]

        for i in range(len(nums)):
            if(i>0 and nums[i] == nums[i-1]):
                    continue
            for j in range(i+1, len(nums)):
                k = len(nums) - 1
                n = j +1
                end = target - nums[i] - nums[j]

                
                if(j > i+1 and nums[j] == nums[j-1]):
                    continue
                    
                while n < k:
                    if(nums[n] + nums[k] < end):
                        n += 1
                    elif(nums[n] + nums[k] > end):
                        k-=1
                    else:
                        h.append([nums[i], nums[j], nums[n], nums[k]])
                        n += 1
                        k-=1

                        while(n < k and nums[n] == nums[n-1]):
                            n+=1
                        while(n<k and nums[k] == nums[k+1]):
                            k-=1
                
        return h
        