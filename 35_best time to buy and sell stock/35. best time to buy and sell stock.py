#make the runtime faster
class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        return max_profit
    
input_string = input("Enter a string: ")
print("Max profit:", Solution().maxProfit(input_string))