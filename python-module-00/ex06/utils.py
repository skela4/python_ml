import string

cookbook = {
    'sandwich': {
        'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal': 'lunch',
        'prep_time': 10
    },
    'cake': {
        'ingredients': ['flour', 'sugar', 'eggs'],
        'meal': 'dessert',
        'prep_time': 60
    },
    'salad': {
        'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
        'meal': 'lunch',
        'prep_time': 15
    }
}


def get_input(text):
    try:
        return input(text).strip(string.whitespace)
    except (EOFError, KeyboardInterrupt):
        raise SystemExit("\ncookbook closed. Goodbye !")


def print_recipe_name():
    print()
    [print(recipe) for recipe in [*cookbook]]


def print_recipe_details():
    name = get_input("\nPlease enter a recipe name to get its details:\n>> ")
    if name in cookbook:
        print(
            f"\nRecipe for {name}\n"
            f"  Ingredients list: {cookbook[name]['ingredients']}\n"
            f"  To be eaten for {cookbook[name]['meal']}\n"
            f"  Takes {cookbook[name]['prep_time']} minutes of cooking."
        )

    
def delete_recipe():
    name = get_input("\nPlease enter a recipe name to delete:\n>> ")
    if name in cookbook:
        del cookbook[name]


def add_recipe():
    name = get_input("\n>>> Enter a name:\n")
    while len(name) == 0:
        name = get_input("\n>>> Enter a name:\n")
    ingredients = []
    ingredient = get_input(">>> Enter ingredients:\n")
    while len(ingredient) == 0:
        ingredient = get_input("\n>>> Enter ingredients:\n")
    ingredients.append(ingredient)
    next_ingredient = get_input('')
    while (next_ingredient != ''):
        ingredients.append(next_ingredient)
        next_ingredient = get_input('')
    meal = get_input(">>> Enter a meal type:\n")
    while len(meal) == 0:
        meal = get_input("\n>>> Enter a meal type:\n")
    prep_time = get_input(">>> Enter a preparation time:\n")
    result = False
    try:
        prep_time = int(prep_time)
        result = True and prep_time >= 0
    except Exception:
        result = False

    while result == False:
        prep_time = get_input("\n>>> Enter a preparation time:\n")
        try:
            prep_time = int(prep_time)
            result = True and prep_time >= 0
        except Exception:
            result = False

    cookbook[name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time
    }

commands = {
    '1': add_recipe,
    '2': delete_recipe,
    '3': print_recipe_details,
    '4': print_recipe_name,
    '5': None,
}

options = {
    '1': 'Add a recipe',
    '2': 'Delete a recipe',
    '3': 'Print a recipe',
    '4': 'Print the cookbook',
    '5': 'Quit'
}

def recipe():
    print("Welcome to the Python Cookbook !")
    [print(k, ': ', v) for k, v in options.items()]
    print()
    user_input = get_input(
        "Please select an option:\n"
            ">> "
    )
    while user_input != None and user_input != '5':
        if user_input not in options.keys():
            print("\nSorry this option does not exist.")
            [print(k, ': ', v) for k, v in options.items()]
        else:
            commands[user_input]()
        user_input = get_input(
            "\nPlease select an option:\n"
            ">> "
        )
    print("\ncookbook closed. Goodbye !")

if __name__ == '__main__':
    recipe()
