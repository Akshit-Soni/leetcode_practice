class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)

        return max_profit


        # min_val = min(prices)
        # min_index = prices.index(min_val)
        
        # if min_index == len(prices):
        #     return 0
        
        # for i in range(min_index+1, len(prices)):
        #     prices[i] = abs(prices[i] - min_val)
        
        # print(prices)

        # max_val = max(prices[min_index+1:len(prices)])

        # return max_val