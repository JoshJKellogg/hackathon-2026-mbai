# You are given a list ```prices``` where ```prices[i]``` is the price of a given stock on the ```i```th day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Write a function ```maxProfit(prices)``` that calculates the maximum profit you can achieve from this transaction. If you cannot achieve any profit, the return value should be ```0```.

 

# Example:
# ```
# Argument: prices = [7,1,5,3,6,4]

# Return value: 5
# ```
# Explanation: Buy on day ```2``` (```price = 1```) and sell on day ```5``` (```price = 6```), ```profit = 6-1 = 5```.
# Note that buying on day ```2``` and selling on day ```1``` is not allowed because you must buy before you sell.

# Another example:

# ```
# Argument: prices = [7,6,4,3,1]
# Return value: 0
# ```
# Explanation: In this case, no transactions are done and the max ```profit = 0```.
 
 
# * Add code that tests your function. Aim for at least 5 tests that test different scenarios (both black-box and clear-box testing).

def maxProfit(prices):
    profit = 0
    max_price = 0
    for price in reversed(prices):
        max_price = max(max_price, price)
        profit = max(profit, max_price - price)
    return profit

print(maxProfit([4,8,3,8,0,10]))
assert maxProfit([1,2,3,4,5]) == 4
assert maxProfit([1]) == 0
assert maxProfit([1,1,1,1,1]) == 0
assert maxProfit([5,4,3,2,1]) == 0