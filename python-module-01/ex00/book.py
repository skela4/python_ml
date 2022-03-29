import string
from datetime import datetime
from recipe import recipe


class Book:
    def __init__(self, name = "book of recipes"):
        self.name = name
        self.creation_date = datetime.now(tz=None)
        self.last_update = datetime.now(tz=None)
        self.recipes_list = {
            "starter" : [],
            "lunch": [],
            "dessert": []
        } # a dictionnary with 3 keys: "starter", "lunch", "dessert"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def creation_date(self):
        return self.creation_date

    @property
    def last_update(self):
        return self._last_update


    def get_recipe_by_name(self, name):
        self._last_update = datetime.now(tz=None)
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

    def __str__(self):
        """Return the string to print with the recipe info"""
        return self.description


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