# GetARecipe
This program is my final project from CodeCademy Computer Science course. I built a recipe recommendation program based on ingredient choice and filtering.
I got my database from shuyangli94 on Kaggle. (tks!)

main.py contains most of the algorithms for dealing with the data:
- retrieving ingredient list from recipe database;
- retrieving recipes by ingredient;
- choosing the ingredient that will filter the recipes most efficiently;
- quicksort (for sorting ingredients, as optimization strategy);
- filtering recipes by ingredient;

and also for dealing with user inputs and searches:
- searching for matches between user input and dataset;
- filter ingredient list based on input;
- Boolean choice test;
- multiple choice printing and retrieving;
 
get_a_recipe is the main program, with the interface logic. There are two "playing" modes:
1) typing ingredient names (or some letters) to filter the recipes;
2) answering "yes or no" to ingredients that are chosen based on the most efficient filtering possible;

both modes work on the same looping logic, in which the user can keep filtering endlessly until they're are satisfied and at each step they're prompt with the number of available recipes with those filters.

Since this was an exercise, I used the random module to get a sample of 10k recipes from the database, that allowed me to work a little faster. I also opted to transform the csv data into a python dictionary, so I wouldn't get caught up in the specifics of data handling, which probably be my next learning subject.
I also didn't worry too much with improving the ingredients in the database to eliminate senseless repetition or any other stuff.

Enjoy and feel free to get in touch to give feedback!

