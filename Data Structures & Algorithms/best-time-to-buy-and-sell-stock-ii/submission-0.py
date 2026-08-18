class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #till the next number is bigger than the 
        #previous one, keep on moving and don't sell
        #buy when the number is the smallest and the next one is 
        #bigger

        #profit till that index
        prev = prices[0]
        profits = {}
        f = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                f += prices[i] - prices[i-1]
        return f
        