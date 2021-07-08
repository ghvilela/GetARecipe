from recipe_dict import recipe_dict
from recipes import Recipe
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
    recipes_by_ingredient = []
    for recipe in recipes:
        if ingredient in recipe.ingredients:
            recipes_by_ingredient.append(recipe)
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

# logic for getting user recipe choice
def choose_recipe(choices, input_text):
  count = 0
  for choice in choices:
    count += 1
    print(f"{count}) {choice.name}\n")
    
  choice_range = [f"{num}" for num in range(1, count+1)]
  user_choice = input(input_text)
  if user_choice not in choice_range:
    print(f"invalid input: please choose from 1 to {count}")
    choose_recipe(choices, input_text)
  else:
    return choices[int(user_choice)-1]

# quicksort function
def quicksort(arr):
   if len(arr) <= 1: return arr
   m = arr[randrange(0,len(arr))]
   return quicksort([i for i in arr if i < m]) + \
          [i for i in arr if i == m] + \
          quicksort([i for i in arr if i > m])

# quick search in sorted list
def check_match(input, text):
  match_count = 0
  for char in range(len(input)):
    if len(input) > len(text):
      return False
    elif input[char] == text[char]:
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
    while start>=0 and check_match(input,list[start]) is True:
      start -= 1
    while end<=(len(list)-1) and check_match(input,list[end]) is True:
      end += 1
  #else call recursive steps
  else:
    if input < list[pivot]:
      return find_match(list[:pivot+1], input)
    return find_match(list[pivot:], input)
  #return sliced list
  return list[start+1:end]


##helper variables and functions
def bolean_test(prompt):
    user_input = input(f"{prompt} [y/n]")
    if user_input.lower() == "y":
        return True
    elif user_input.lower() == "n":
        return False
    else:
        return bolean_test(prompt)

def get_choice(choices, input_text):
  count = 0
  for choice in choices:
    count += 1
    print(f"{count}) {choice}\n")
    
  choice_range = [f"{num}" for num in range(1, count)]
  user_choice = input(input_text)
  if user_choice not in choice_range:
    print(f"invalid input: please choose from 1 to {count}")
    return get_choice(choices, input_text)
  else:
    return choices[int(user_choice)-1]

#ingredient filtering logic
def ingredient_filtering(ingredient_list):
    search_ingredient_input = input("Type the first letter or first few letters of the ingredient you are looking for:")
    match = find_match(ingredient_list, search_ingredient_input)
    if type(match) is list:
        print("\nMatches found:\n")
        for i in match: 
            print (i)
        test = bolean_test("Want to filter some more?")
    elif type(match) is str:
        print(match)
        test = False    
    if test is True:
        return ingredient_filtering(match)
    else:
        if type(match) is list:
            return match
        return ingredient_list

#recipe filtering logic
def filter_recipes(ingredients, recipes):
    recipes_filtered = []
    for i in ingredients:
        subset = get_recipes_by_ingredient(recipes, i)
        for r  in subset:
            if r not in recipes_filtered:
                recipes_filtered.append(r)
    return recipes_filtered
