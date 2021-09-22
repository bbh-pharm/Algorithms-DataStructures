prices = [7, 1, 5, 3, 6, 4]

#################
## Brute-force ##
#################
def max_profit(prices):
  max_price = 0

  for i, price in enumerate(prices):
    for j in range(i, len(prices)):
      max_price = max(prices[j] - price, max_price)
  return max_price

#################
## O(n) method ##
#################
import sys

def max_profit(prices):
  profit = 0
  min_price = sys.maxsize

  for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

  return profit

max_profit(prices)
