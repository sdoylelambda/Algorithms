#!/usr/bin/python

import argparse

#   track of the `current_min_price_so_far` and the `max_profit_so_far`?

# prices = [10, 7, 5, 8, 11, 9]
# # return 6     === (11 - 5)
# print('prices in', prices)

def find_max_profit(prices):
  # take in list, find largest difference between numbers and return it
  maxPrice = max(prices)
  current_min_price_so_far = 0;
  max_profit_so_far = 0;
  # print('maxPrice', maxPrice)
  for i in prices:
    # print(i)
    for x in prices:
      # print(x)
      if i - x > current_min_price_so_far:
        current_min_price_so_far = i - x
        # print('current_min_price_so_far', current_min_price_so_far)

  return current_min_price_so_far

# find_max_profit(prices)



# *********** UNCOMMENT THIS OUT TO RUN TESTS ************

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))