# In this we need to find the maximum profit each day generated as on one day we will buy the plot and the other day we would sell can't do both on same day so find the maximum profit on which genrated on differnt days.
#approach : firslty we will store a single value that would be first index by applying pop on our given list of prices and mark max and profit as zero followed by iterating through the prices in such a way that when we compare the min value to prices if prices value is les than min then return to min to price and max will be zero and further if price value is greater than max return price as max and the if diff of max and min is greater than profit then profit is equal to diff of max to min and then return the profit to main fuction.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices.pop(0)
        max=0
        profit =0
        for price in prices:
            if price < min:
                min = price
                max=0
            elif price > max:
                max=price
                if max-min > profit:
                    profit = max-min
        return profit

        