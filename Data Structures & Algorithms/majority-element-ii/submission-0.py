class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #store it in a dict and keep on adding the counts
        #as soon as the count hits more than n/3 push to the list

        d = {}
        f = []

        for i in range(len(nums)):
            
            if nums[i] not in d:
                d[nums[i]] = d.get(nums[i], 0) + 1
            else:
                d[nums[i]] += 1
        print(d, len(nums)//3)
        for i in d:
            print(d[i])
            if d[i] > len(nums) // 3:
                f.append(i)
        return f
        