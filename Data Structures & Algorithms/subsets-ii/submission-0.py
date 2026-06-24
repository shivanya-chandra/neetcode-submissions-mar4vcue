class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(i, cur):
            if i>= len(nums):
                if cur.copy() not in res:
                    res.append(cur.copy())
                    return
                return
            # if cur.copy() in res:
            #     return

            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            while(i+1 < len(nums) and nums[i+1] == nums[i]):
                i = i+1
            dfs(i+1, cur)
        dfs(0, [])
        return res
        