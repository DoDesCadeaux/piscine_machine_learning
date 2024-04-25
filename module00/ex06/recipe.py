sandwich = {
    "ingredients": ["ham", "bread", "cheese", "tomatoes"],
    "meal": "lunch",
    "prep_time": 10
}


cake = {
    "ingredients": ["flour", "sugar", "eggs"],
    "meal": "dessert",
    "prep_time": 60
}

salad = {
    "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
    "meal": "lunch",
    "prep_time": 15
}

cookbook = {
    "sandwich": sandwich,
    "cake": cake,
    "salad": salad
}


def print_cookbook():
    for recipe in cookbook.keys():
        print(recipe)


def recipe_details(recipe):
    print(f"\nRecipe for : {recipe}")
    print(f"Ingredients list: {cookbook[recipe].get("ingredients")}")
    print(f"To be eaten for {cookbook[recipe].get("meal")}.")
    print(f"Takes {cookbook[recipe].get("prep_time")} minutes of cooking.\n")


def delete_recipe(recipe):
    cookbook.pop(recipe)


def add_recipe():
    new_recipe = dict()
    recipe_name = str(input("Enter a name:"))
    recipe_ingredients = list()

    while True:
        ingredient = input("Enter ingredients: ")
        if ingredient:
            recipe_ingredients.append(ingredient)
        else:
            break

    recipe_meal = input("Enter a meal type: ")
    recipe_preparation = input("Enter a preparation time: ")

    new_recipe.setdefault("ingredients", recipe_ingredients)
    new_recipe.setdefault("meal", recipe_meal)
    new_recipe.setdefault("prep_time", recipe_preparation)

    cookbook.setdefault(str(recipe_name), new_recipe)


def print_options():
    print("List of available options:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")


def select_options():
    option = 0
    while True:
        try:
            option = int(input("Please select an option:\n"))
            if not 1 <= option < 6:
                print("Sorry this option doesn't exists")
                continue
        except ValueError:
            print("Sorry this option doesn't exists")
            continue
        break
    return option


def main():
    print("Welcome to the Python Cookbook!")
    while True:
        print_options()
        option = select_options()
        if option == 1:
            add_recipe()
        elif option == 2:
            try:
                recipe = str(input("Enter a recipe name to delete:\n"))
                delete_recipe(recipe)
            except ValueError:
                print("Sorry this recipe doesn't exists")
                continue
        elif option == 3:
            try:
                recipe = input("Enter recipe name to get its details:\n")
                if recipe not in cookbook:
                    print("Sorry this recipe doesn't exists\n")
                    continue
                recipe_details(recipe)
            except ValueError:
                print("Sorry this recipe doesn't exists\n")
        elif option == 4:
            print_cookbook()
        elif option == 5:
            exit(0)


if __name__ == "__main__":
    main()
