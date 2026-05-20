class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minStock = float('inf')
        maxProfit = 0
        
        for price in prices:
            minStock = min(minStock, price)
            profit = price - minStock
            maxProfit = max(maxProfit, profit)
        
        return maxProfit