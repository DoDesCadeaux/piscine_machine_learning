from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name: str, last_update: datetime, creation_date: datetime, recipe_list: dict):
        if not isinstance(name, str) and not name:
            raise ValueError("name must be a non-empty string")
        if not isinstance(last_update, datetime) or not last_update:
            raise ValueError("last update must be a non-empty datetime")
        if not isinstance(creation_date, datetime) or not creation_date:
            raise ValueError("creation date must be a non-empty datetime")
        if not isinstance(recipe_list, dict) or (list(recipe_list) != ["starter", "lunch", "dessert"]) or not recipe_list:
            raise ValueError("recipe list must be a non-empty dictionnary with 3 keys as: starter lunch and dessert")

        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipe_list = recipe_list

    def __str__(self):
        return f"Book: {self.name}"

    def get_recipe_by_name(self, name):
        for recipe in self.recipe_list.values():
            if name == recipe.name:
                return recipe
        raise ValueError("recipe doesn't exists in the Cookbook")

    def get_recipes_by_types(self, recipe_type):
        recipes = []
        for recipe in self.recipe_list.values():
            if recipe_type == recipe.recipe_type:
                recipes.append(recipe.name)
        if not recipes:
            return f"No recipes with {recipe_type} type"
        return recipes

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe) or not recipe:
            raise ValueError("Must be a valid non-empty Recipe object to add")
        self.recipe_list[recipe.recipe_type] = recipe
        self.last_update = datetime.now()
