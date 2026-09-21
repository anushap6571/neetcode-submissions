class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = prices[r] - prices[l]
                maxPrice = max(maxPrice, prices[r] - prices[l])
            r +=1
            print(maxPrice)
            
        
        return maxPrice