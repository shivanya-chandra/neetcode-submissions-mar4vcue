class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            d = {}
            a = []
            for i in range(len(nums)):
                if target - nums[i] in d:
                    a.append(d[target - nums[i]])
                    a.append(i)
                d[nums[i]] = i
            return a