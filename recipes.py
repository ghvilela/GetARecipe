class Recipe():
    def __init__(self, dict, id):
        self.id = id
        self.name = dict["name"]
        self.minutes = dict["minutes"]
        self.steps = eval(dict["steps"])
        self.ingredients = eval(dict["ingredients"])
    
    def has_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def __str__(self):
        print(self.name.title() + "\n")
        print(f"Preparation time: {self.minutes} minutes \n")
        print("Ingredients:")
        for i in self.ingredients:
            print(f"- {i};")
        print("\nPreparation Steps:")
        for s in self.steps:
            print (f"- {s};")
        return ""

