import string
class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, recipe_type, description = ''):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        assert isinstance(value, str), "name need to be a string"
        assert len(value) > 0, "name cannot be empty"
        self._name = value

    @property
    def cooking_lvl(self):
        return self._cooking_lvl

    @cooking_lvl.setter
    def cooking_lvl(self, value):
        assert isinstance(value, int), "cooking level need to be a integer"
        assert value >= 0 and value <= 5 , "range from 1 to 5"
        self._cooking_lvl = value

    @property
    def cooking_time(self):
        return self._cooking_time

    @cooking_time.setter
    def cooking_time(self, value):
        assert isinstance(value, int), "(int) cooking_time need to be a integer"
        assert value >= 0, "(int) range from 0 to infinity"
        self._cooking_time = value

    @property
    def ingredients(self):
        return self._ingredients

    @ingredients.setter
    def ingredients(self, value):
        assert isinstance(value, list), "ingredients need to be a list"
        for e in value:
            assert isinstance(e, str), "ingredients need to be a string"
            assert len(e.strip(string.whitespace)) > 0, "ingredients in list cannot be empty"
        self._ingredients = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        assert isinstance(value, str), "description need to be a string"
        self._description = value

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, value):
        assert value in ['starter', 'lunch', 'dessert'], 'can be "starter", "lunch" or "dessert" '
        self._recipe_type = value

    def __str__(self):
        def each(lst):
            result = ''
            for e in lst:
                result += f"{e} "
            return result
        return f"Description: {self.description}\n"\
        f"A recipe made of {each(self.ingredients)}to be eat at {self.recipe_type} "\
        f"It takes {self.cooking_time} to cook for at level {self.cooking_lvl}"

    def __repr__(self):
        return  "Recipe("\
        "name='tourte', "\
        "cooking_lvl=2, "\
        "cooking_time=60, "\
        "ingredients=['oil', 'vfd'], "\
        "recipe_type='starter', "\
        "description='une simple tourte')"


if __name__ == '__main__':
    try:
        tourte = Recipe(name='tourte', cooking_lvl=2, cooking_time=60, ingredients=['oil', 'tomato'], recipe_type='starter', description='une simple tourte')
        print(tourte)
        print(str(tourte))
        print(repr(tourte))
        print(tourte.name)
        pass
        # name = tourte.get_name()
        # print(name)
        # tourte.get_cooking_lvl()
        # tourte.get_cooking_time()
        # tourte.get_ingredients()
        # tourte.get_recipe_type()
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")