class Solution:
    def search(self, nums: List[int], target: int) -> int:
        found = False
        f = -1
        for i in range(len(nums)):
            if(target == nums[i]):
                found = True
                f=i
                return i
            else:
                found =False
                f=-1
        if(found):
            return f
        else:
            return -1
        