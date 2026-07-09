class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = nums[0]
        res = nums[0]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            s = max(s+nums[i], nums[i])
            res = max(res,s)
        return res

        