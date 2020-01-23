#!/usr/bin/python

import math

# SAMPLE INPUT
recipes = {
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}

ingredients = {
  'eggs': 5,
  'butter': 10,
  'sugar': 8,
  'flour': 15
}
# EXPECTED SAMPLE RETURN === 0

def recipe_batches(recipes, ingredients):
  # UPER
  # - UNDERSTAND
  # TAKE IN RECIPE AND INGREDIENTS DICTIONARIES
  # SEE HOW MANY DISHES CAN BE MADE FROM COMPARING INPUTS
  # RETURN INT FOR HOW MANY DISHES CAN BE MADE
  # P - PLAN
  # compare each position of the dictionary(a) to the next dictionary(b)
  #   return a // b
  #   do for each item in dictionary
  #   final return smallest number from above


  for recipe in recipes:
    r = recipe
    print(r)
    print(recipes.get(r))


recipe_batches(recipes, ingredients)













# PUT BACK IN TO RUN TESTS

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))