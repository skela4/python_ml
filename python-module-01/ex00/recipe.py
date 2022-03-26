class Recipe:
    def __init__(self, name, description = ''):
        self.name = name
        self.cooking_lvl = int
        self.cooking_time = int
        self.description = description
        self.ingredients = list
        self.recipe_type = str

    def __str__(self):
        return self.description
        pass

    def get_name(self):
        assert isinstance(self.name, str), "name need to be a string"
        assert len(self.name) > 0, "name cannot be empty"
        return self.name

    def get_cooking_lvl(self):
        assert isinstance(self.cooking_lvl, int), "(int) name need to be a integer"
        assert self.cooking_lvl >= 0 and self.cooking_lvl <= 5 , "(int) range from 1 to 5"
        return self.cooking_lvl

    def get_cooking_time(self):
        assert isinstance(self.cooking_time, int), "(int) name need to be a integer"
        assert self.cooking_time >= 0, "(int) range from 0 to infinity"
        return self.cooking_time

    def get_ingredients(self):
        # assert isinstance(self.ingredients, list), "(list) list of all ingredients each represented by a string"
        # [assert isinstance(ingredient, str) for ingredient in self.ingredients]

        print([isinstance(ingredient, str) for ingredient in self.ingredients])
        # assert all([isinstance(e, int) for e in kata]), (
        #     "value in tuple can only be a integer"
        # )
        return self.ingredient


if __name__ == '__main__':
    tourte = Recipe('tourte', 'une simple tourte')
    try:
        name = tourte.get_name()
        print(name)
        tourte.get_cooking_lvl()
        tourte.get_ingredients()
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")