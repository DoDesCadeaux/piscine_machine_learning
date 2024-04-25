class Recipe:
    def __init__(self, name: str, lvl: int, time: int, ingredients: list, r_type: str, description=None):
        if not isinstance(name, str) or not name:
            raise ValueError("name must be a non-empty string.")
        if not isinstance(lvl, int) or not (1 <= lvl <= 5) or not lvl:
            raise ValueError("cooking level must be a integer between 1 and 5")
        if not isinstance(time, int) or (time < 0) or not time:
            raise ValueError("time must be a positive integer.")
        if not isinstance(ingredients, list) or not ingredients or not (all(isinstance(ing, str) for ing in ingredients)):
            raise ValueError("ingredients must be a list of string")
        if r_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe type must be starter, lunch or dessert")

        self.name = name
        self.cooking_lvl = lvl
        self.cooking_time = time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = r_type

    def __str__(self):
        return f"Recipe: {self.name}"


def main():
    try:
        pizza = Recipe(name="Pizza", lvl=5, time=30, ingredients=["Pate", "Fromage", "Tomate"], r_type="lunch")
        print(pizza)
    except ValueError as v:
        print(v)
        exit(1)


if __name__ == "__main__":
    main()
