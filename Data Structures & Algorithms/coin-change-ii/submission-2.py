class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        d = set()
        self.c = 0
        cache = {}
        def dfs(i, amt):
            if amt == 0:
                return 1
            if i== len(coins) or amt<0:
                return 0
            if (i,amt) in cache:
                return cache[(i,amt)]
            else:
            
            
                use=dfs(i, amt-coins[i])
                skip=dfs(i+1, amt)
                cache[(i,amt)] = use+skip
                return cache[(i,amt)]
        return dfs(0, amount)
