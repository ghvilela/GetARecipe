import csv
import sys

new_file = open("recipe_dict.py", "w")
sys.stdout = new_file

recipes_dict = []
recipes_data = csv.DictReader(open("C:/Users/BH/Desktop/GetARecipe/data/recipes_sample.csv"))
for line in recipes_data:
    recipes_dict.append(line)

print(recipes_dict)