class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = 0
        far = 0
        jumps = 0

        for i in range(len(nums)-1):
            far = max(far, nums[i]+i)

            if i == curr:
                jumps+=1
                curr=far
        return jumps
    
            



        