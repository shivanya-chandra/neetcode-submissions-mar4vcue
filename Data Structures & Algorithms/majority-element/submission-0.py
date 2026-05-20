class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        m = 0
        k = 0
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for i in dic.keys():
            if dic[i] > m:
                m = dic[i]
                k = i
        return k
        