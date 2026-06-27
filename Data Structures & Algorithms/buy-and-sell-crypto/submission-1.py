class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res = 0

        for each_buy in range(len(prices)):

            for each_sell in range(each_buy+1, len(prices)):
                
                res = max(res, prices[each_sell] - prices[each_buy])

        return res