class Recipe:
    def __init__(self, name, recipe_type, cooking_lvl, cook description = ''):
        self.name = name
        self.cooking_lvl = int(0)
        self.cooking_time = int
        self.ingredients = list(['vdf','vfd','vfd', 'vfd'])
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return self.description
        pass

    def get_name(self):
        assert isinstance(self.name, str), "name need to be a string"
        assert len(self.name) > 0, "name cannot be empty"
        return self.name

    def get_cooking_lvl(self):
        assert isinstance(self.cooking_lvl, int), "cooking level need to be a integer"
        assert self.cooking_lvl >= 0 and self.cooking_lvl <= 5 , "range from 1 to 5"
        return self.cooking_lvl

    def get_cooking_time(self):
        assert isinstance(self.cooking_time, int), "(int) name need to be a integer"
        assert self.cooking_time >= 0, "(int) range from 0 to infinity"
        return self.cooking_time

    def get_ingredients(self):
        to_assert = [isinstance(self.ingredients, list)]
        [to_assert.append(isinstance(e, str)) for e in self.ingredients]
        assert all(to_assert), "list of all ingredients each represented by a string"
        return self.ingredients
    
    def get_recipe_type(self):
        accept_recipe_type = ['starter', 'lunch', 'dessert']
        to_assert = [self.recipe_type == type_recipe for type_recipe in accept_recipe_type]
        assert any(to_assert), 'can be "starter", "lunch" or "dessert" '
        return self.recipe_type


if __name__ == '__main__':
    tourte = Recipe('tourte', 'starter', 'une simple tourte')
    try:
        name = tourte.get_name()
        print(name)
        tourte.get_cooking_lvl()
        tourte.get_ingredients()
        tourte.get_recipe_type()
    except AssertionError as error:
        raise SystemExit(f"{AssertionError.__name__}: {error}")