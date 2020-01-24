#!/usr/bin/python

import math

# 'milk': 100, 'flour': 4, 'sugar': 10, 'butter': 5 }, { 'milk': 1288, 'flour': 9, 'sugar': 95

# SAMPLE INPUT
recipes = {
  'milk': 100, 'butter': 50, 'cheese': 10
}

ingredients = {
  'milk': 1948, 'butter': 542, 'cheese': 20
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
  # x = 0
  # recipes[x] - ingredients[x]
  numOfBatches = 0

  # for recipe in recipes:
  #   r = recipe
  #   # print(r)
  #   print(recipes.get(r))
  #
  #   for ingredient in ingredients:
  #     i = ingredient
  #     print(ingredients.get(i))
  #
  #     recipes[r] - ingredients[i]
  #     if recipes[r] > 0:
  #         print('r', recipes[r])

  max_batches = 0
  for recipe_ingredient in recipes:
    if recipe_ingredient not in ingredients:
      print('nothing')
      return 0
    elif recipe_ingredient in ingredients:
      current_max = ingredients[recipe_ingredient] // recipes[recipe_ingredient]
      print('x',current_max)
      if current_max <= 0:
        return 0
      elif max_batches == 0 or current_max < max_batches and recipe_ingredient not in ingredients:
        max_batches = current_max
      print(max_batches)
      return max_batches

recipe_batches(recipes, ingredients)















# PUT BACK IN TO RUN TESTS

# if __name__ == '__main__':
#   # Change the entries of these dictionaries to test
#   # your implementation with different inputs
#   recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
#   ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
#   print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))