import string
from datetime import datetime

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ''):
        self.name = self.set_name(name)
        self.cooking_lvl = self.set_cooking_lvl(cooking_lvl)
        self.cooking_time = self.set_cooking_time(cooking_time)
        self.ingredients = self.set_ingredients(ingredients)
        self.description = self.set_description(description)
        self.recipe_type = self.set_recipe_type(recipe_type)

    def __str__(self):
        return self.description
        pass

    def set_name(self, name):
        assert isinstance(name, str), "name need to be a string"
        assert len(name) > 0, "name cannot be empty"
        return name

    def set_cooking_lvl(self, cooking_lvl):
        assert isinstance(cooking_lvl, int), "cooking level need to be a integer"
        assert cooking_lvl >= 0 and cooking_lvl <= 5 , "range from 1 to 5"
        return cooking_lvl

    def set_cooking_time(self, cooking_time):
        assert isinstance(cooking_time, int), "(int) name need to be a integer"
        assert cooking_time >= 0, "(int) range from 0 to infinity"
        return cooking_time

    def set_ingredients(self, ingredients):
        assert isinstance(ingredients, list), "ingredients need to be a list"
        to_assert = []
        for e in ingredients:
            assert isinstance(e, str), "element in ingredients need to be a string"
            assert len(e.strip(string.whitespace)) > 0, (
                "element in ingredients cannot be empty"
            )
        return ingredients

    def set_description(self, description):
        assert isinstance(description, str), "description need to be a string"
        return description

    def set_recipe_type(self, recipe_type):
        to_assert = [recipe_type == e for e in ['starter', 'lunch', 'dessert']]
        assert any(to_assert), 'can be "starter", "lunch" or "dessert" '
        return recipe_type

class Book:
    def __init__(self, name = "book of recipes"):
        self.name = name # name of the book
        self.last_update = datetime.now(tz=None) # the date of the last update
        self.creation_date = datetime.now(tz=None) # the creation date
        self.recipes_list = {
            "starter" : [],
            "lunch": [],
            "dessert": []
        } # a dictionnary with 3 keys: "starter", "lunch", "dessert"

    def __str__(self):
        """Return the string to print with the recipe info"""
        return ""
        pass

    def get_recipe_by_name(self, name):

        for k, v in self.recipes_list.items():
            print(k, v)
        # recipe_list = [
        #     *self.recipes_list["starter"],
        #     *self.recipes_list["lunch"],
        #     *self.recipes_list["dessert"]
        # ]
        # for e in recipe_list:
        #     yield e

        # for e in generator():
        #     if e.name == name:

        #     print(e.name)
        #     # recipe_list.append(*e)
            # recipe_list = [*recipe_list, *v]
            # print(recipe_list)


        # for e in recipe_list:
        #     if e.name == name:
        #         return e
        # return None

    def get_recipes_by_types(self, recipe_type):
        return self.recipes_list[recipe_type]

    def add_recipe(self, recipe):
        assert isinstance(recipe, Recipe), "recipe need to be an instance of Recipe Class"
        recipe_type = recipe.recipe_type
        self.recipes_list[recipe_type].append(recipe)
        return None


if __name__ == '__main__':
    try:
        tourte = Recipe(
            name='tourte', cooking_lvl=2, cooking_time=60, ingredients=['oil', 'potatoes'], recipe_type='starter', description='une simple tourte'
        )
        # tourte = Recipe(
        #     name='tourte', cooking_lvl=2, cooking_time=60, ingredients=['oil', 'potatoes'], recipe_type='starter', description='une simple tourte'
        # )
        # name = tourte.get_name()
        # print(name)
        # print(tourte.get_cooking_lvl())
        # print(tourte.get_cooking_time())
        # print(tourte.get_ingredients())
        # print(tourte.get_recipe_type())
        first_book = Book()
        first_book.add_recipe(tourte)
        recipe = first_book.get_recipe_by_name('tourt')
        # print(recipe)
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")