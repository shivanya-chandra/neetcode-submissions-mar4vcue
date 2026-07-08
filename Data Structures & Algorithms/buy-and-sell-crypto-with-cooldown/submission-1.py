class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp={}

        def dfs(i, can_buy):
            if i >= len(prices):
                return 0

            if (i, can_buy) in dp:
                return dp[(i,can_buy)]

            if can_buy:
                buy = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, True)
                dp[(i, can_buy)] = max(buy,cooldown)
            else:
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False)
                dp[(i, can_buy)] = max(sell,cooldown)
            return dp[(i, can_buy)]
        return dfs(0, True)
            
            
            

            

            
        