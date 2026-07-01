class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def recur(i):
            if i == n:
                return 1
            if i > n:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = recur(i+1) + recur(i+2)
            return cache[i]
        
        return recur(0)
        