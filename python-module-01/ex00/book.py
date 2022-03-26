class Book:
    name = str
    last_update = datetime
	creation_date = datetime
    recipes_list = {
		"starter" : "",
		"lunch": "",
		"dessert": ""
	}
    def __init__(self):
        pass

    def __str__(self):
        """Return the string to print with the recipe info"""
        return ""
        pass

	def get_recipe_by_name(self, name):
		print()

	def hello(self):
		print('helo from book')


if __name__ == '__main__':
    tourte = Recipe()