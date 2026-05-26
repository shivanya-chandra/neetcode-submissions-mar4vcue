class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        k = 200000
        s=0
        left = 0
        for right in range(len(nums)):
            s+= nums[right]

            while s >= target:
                k = min(k, right-left +1)
                s -= nums[left]
                left+=1
        if(k==200000):
            return 0

        return k
        