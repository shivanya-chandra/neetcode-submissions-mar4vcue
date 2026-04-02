class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num={}
        ret = []
        newRet = []

        if(len(nums) == 1):
            return nums

        for i in nums:
            key = i

            if key not in num:
                num[key] = 0
            
            num[key] += 1
        
        freq = []

        for key in num:
            freq.append((num[key], key))


        freq.sort(reverse=True)


        ret = []
        for i in range(k):
            ret.append(freq[i][1])

        return ret