class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # 0(n2)        
        # res = 0

        # for each_buy in range(len(prices)):

        #     for each_sell in range(each_buy+1, len(prices)):
                
        #         res = max(res, prices[each_sell] - prices[each_buy])

        # return res

        # Two pointers
        l = 0
        r = 1
        maxP= 0

        while r < len(prices):
            profit = 0
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
            else:
                l = r

            maxP = max(maxP, profit)
            r+=1
        
        return maxP

