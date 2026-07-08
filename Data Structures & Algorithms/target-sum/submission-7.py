class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache={}
        c = 0
        def dfs(i, res):
            if i== len(nums):
                if res == target:
                    return 1
            # if res > target or res < target:
                return 0
           
            if (i,res) in cache:
                return cache[(i, res)]
            cache[(i, res)] = dfs(i+1, res+nums[i]) + dfs(i+1, res-nums[i])

            return cache[(i,res)]

        return dfs(0, 0)            

            
        