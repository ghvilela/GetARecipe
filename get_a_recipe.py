from random import sample
from typing import List
from main import *
from cfonts import render

##Print Welcome message

title = "Get'A Recipe"
title_message = """
Welcome to Get'A Recipe, the Recipe suggestion app that will blow your...kitchen?!
"""
print(render(title))
print(title_message)

## main logic for type ingredient mode
def type_mode():
    print("Let's find the ingredient you are looking for...")
    keep_choosing = True
    recipes = recipe_list
    ingredient_list = get_ingredient_list(recipe_list)
    ingredients_sorted = quicksort(ingredient_list)
    while keep_choosing:
        ingredients = ingredient_filtering(ingredients_sorted)
        recipes = filter_recipes(ingredients, recipes)
        ingredient_list = get_ingredient_list(recipes)
        ingredients_sorted = quicksort(ingredient_list)
        print(f"\nWe have {len(recipes)} recipes with those ingredients.")
        keep_choosing = bolean_test("Want to choose other ingredients?")
    if len(recipes) > 5:
        recipe_choice_list = sample(recipes, 5)
    else:
        recipe_choice_list = recipes
    print("\nHere are a few suggestions! Choose one and good luck!")
    chosen_recipe = choose_recipe(recipe_choice_list, "Ok! Just choose one of those!")
    print(chosen_recipe)

## main logig for yes/no mode
def yes_no_mode():
    pass

## Get an input on suggestion mode
choose_mode = "Please, choose a suggestion mode:"
modes_list = ["Type an ingredient", "Yes or No"]
suggestion_mode = get_choice(modes_list, choose_mode)

# Based on suggestion mode, run suggestion logic
if suggestion_mode == modes_list[0]:
    type_mode()
else:
    yes_no_mode()
