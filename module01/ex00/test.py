from recipe import Recipe
from book import Book
from datetime import datetime


def main():
    today = datetime.now()
    creation = datetime(2020, 1, 1)

    moules = Recipe(name="moules", lvl=1, time=60, ingredients=["moules"], r_type="starter")
    pizza = Recipe(name="pizza", lvl=1, time=30, ingredients=["pates", "tomates", "fromage"], r_type="lunch")
    glace = Recipe(name="glace", lvl=2, time=300, ingredients=["whatever"], r_type="dessert")

    recipe_dict = {
        "starter": moules,
        "lunch": pizza,
        "dessert": glace
    }

    chips = Recipe(name="chips", lvl=1, time=30, ingredients=["apple of the world"], r_type="starter")

    try:
        cookbooky = Book(name="Cookbooky Tome 1", last_update=today, creation_date=creation, recipe_list=recipe_dict)
        mouleton = cookbooky.get_recipe_by_name("moules")
        recipes_by_type = cookbooky.get_recipes_by_types("starter")
        cookbooky.add_recipe(chips)

        print(mouleton)
        print(recipes_by_type)
        print(cookbooky.get_recipes_by_types("starter"))
    except ValueError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
