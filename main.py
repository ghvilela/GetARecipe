from recipes import Recipe
from recipe_dict import recipe_dict
from math import inf
from random import randrange

##create Recipe instances from dictionary
recipe_list = []

for i in recipe_dict:
    id = i["id"]
    id = Recipe(i, id)
    recipe_list.append(id)


#ingredient list function
def get_ingredient_list(recipes):
    ingredient_list = []
    for recipe in recipes:
        for ingredient in recipe.ingredients:
            if ingredient not in ingredient_list:
                ingredient_list.append(ingredient)
    return ingredient_list


#ingredient count function
def get_ingredient_count(recipes):
  ingredient_count = {}
  for recipe in recipes:
    for ingredient in recipe.ingredients:
      if ingredient not in ingredient_count.keys():
        ingredient_count[ingredient] = 1
      else:
        ingredient_count[ingredient] += 1
  return ingredient_count

#def recipe_by_ingredient function
def get_recipes_by_ingredient(recipes, ingredient):
    recipes_by_ingredient = {}
    recipes_by_ingredient[ingredient] = []
    for recipe in recipes:
        if ingredient in recipe.ingredients:
            recipes_by_ingredient[ingredient].append(recipe.name)
    return recipes_by_ingredient

# ingredient for optimal subset function
def get_optimal_ingredient(recipes):
  best_subset_possible = len(recipes)//2
  optimal_ing = ""
  optimal_count = inf
  ingredient_count = get_ingredient_count(recipes)
  for ingredient, count in ingredient_count.items():
    if abs(best_subset_possible - count) < abs(best_subset_possible - optimal_count):
      optimal_ing = ingredient
      optimal_count = count
  return optimal_ing

# quicksort function
def quicksort(arr):
   if len(arr) <= 1: return arr
   m = arr[randrange(0,len(arr))]
   return quicksort([i for i in arr if i < m]) + \
          [i for i in arr if i == m] + \
          quicksort([i for i in arr if i > m])

# # find ingredient by input funtion (replaced by find_match + check_match)
# def find_ingredients(list, input):
#     match_list = []
#     for ingredient in list:
#         match_count = 0
#         for index in range(len(input)):
#             if input[index] == ingredient[index]:
#                 match_count += 1
#             else:
#                 break
#         if match_count == len(input):
#             match_list.append(ingredient)
#     return match_list

# quick search in sorted list
def check_match(input, text):
  match_count = 0
  for char in range(len(input)):
    if input[char] == text[char]:
      match_count += 1
    else:
      break
  if match_count == len(input):
    return True
  return False

def find_match(list, input):
  #base case
  if len(list) == 1:
    if check_match(input,list[0]) is True:
      return list[0]
    return "no match found..."
  #define slicers
  pivot = len(list)//2
  start = pivot
  end = pivot
  #check for match
  if check_match(input,list[pivot]) is True:
    while check_match(input,list[start]) is True and start>=0:
      start -= 1
    while check_match(input,list[end]) is True and end<=len(list):
      end += 1
  #else call recursive steps
  else:
    if input[0] < list[pivot][0]:
      return find_match(list[:pivot+1], input)
    return find_match(list[pivot:], input)
  #return sliced list
  return list[start+1:end]


# #instantiate recipe list and recipe_by_ingredient dict
# ingredient_list = get_ingredient_list(recipe_list)
# recipe_by_ingredient = get_recipes_by_ingredient(recipe_list, ingredient_list[32])

# #set optimal subset of recipes based on ingredient count and return list of recipes with that ingredient
# optimal = get_optimal_ingredient(recipe_list)
# salt_recipes = get_recipes_by_ingredient(recipe_list, optimal)
# print(salt_recipes)

# # instantiate ingredient list and sort it with quicksort
# ingredient_list = get_ingredient_list(recipe_list)
# sorted_list = quicksort(ingredient_list)
# for i in range(50):
#     print(sorted_list[i])

# # print a list of matching ingredients based on user input
# ingredient_list = get_ingredient_list(recipe_list)
# match_list = find_ingredients(ingredient_list, input("say something"))
# for i in match_list:
#     print(i)

# # test find_match
# ingredient_list = get_ingredient_list(recipe_list)
# sorted_ingredients = quicksort(ingredient_list)
# match_list = find_match(sorted_ingredients, input("say something"))
# for i in match_list:
#     print(i)

# # test check match
# test = check_match("abc","dceabc")
# print(test)
