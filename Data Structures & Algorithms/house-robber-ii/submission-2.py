class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        arr1 = nums[:-1]   # includes first, excludes last
        arr2 = nums[1:]    # excludes first, includes last
        rob1, rob2 = 0,0

        for n in arr1:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        rob3, rob4 = 0,0
        for n in arr2:
            temp = max(n + rob3, rob4)
            rob3 = rob4
            rob4 = temp

        return max(rob2,rob4)
        