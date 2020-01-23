#!/usr/bin/python

import argparse

#   track of the `current_min_price_so_far` and the `max_profit_so_far`?

prices = [10, 7, 5, 8, 11, 9]
# # return 6     === (11 - 5)
# print('prices in', prices)

def find_max_profit(prices):
  max_profit = 0
  for x in prices:
      for y in prices:
        print(y)

  return max_profit

find_max_profit(prices)