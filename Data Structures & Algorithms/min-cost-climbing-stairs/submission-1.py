class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {}
        def recur(i):
            if i>= len(cost):
                return 0
            if i in cache:
                return cache[i]
            # self.c = self.c + min(recur(i+1), recur(i+2))
            cache[i] = cost[i] + min(recur(i+1), recur(i+2))
            return cache[i]
      

        return min(recur(0), recur(1))
        