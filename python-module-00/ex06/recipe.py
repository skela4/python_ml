import string
import re


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


def not_empty_string(str):
    return len(str) > 0


def print_dict_keys(cookbook):
    if isinstance(cookbook, dict):
        for key in cookbook.keys():
            print(key)


def print_dict_values(cookbook):
    if isinstance(cookbook, dict):
        for value in cookbook.values():
            print(value)


def print_dict_items(cookbook):
    if isinstance(cookbook, dict):
        for items in cookbook.items():
            print(items)


def print_recipe(recipe):
    if len(cookbook) == 0:
        print("cookbook is empty")
    elif recipe not in cookbook.keys():
        print("recipe not in cookbook")
    else:
        print(
            f"\nRecipe for {recipe}:\n"
            f"  Ingredients list: {cookbook[recipe]['ingredients']}\n"
            f"  To be eaten for {cookbook[recipe]['meal']}\n"
            f"  Takes {cookbook[recipe]['prep_time']} minutes of cooking."
        )


def delete_recipe(recipe):
    if recipe not in cookbook.keys():
        print("recipe not in cookbook")
    else:
        print(f"Deleting {recipe} from cookbook:")
        del cookbook[recipe]
        print_dict_items(cookbook)


def add_recipe(recipe, ingredients, meal, prep_time):
    delimiters = "|".join(string.whitespace)
    recipe = recipe.strip(string.whitespace)
    meal = meal.strip(string.whitespace)
    # ingredients = re.sub(f'[{string.punctuation}]', '', ingredients)
    # ingredients = list(
    #     filter(not_empty_string, re.split(delimiters, ingredients)))
    prep_time = prep_time.strip(string.whitespace)
    if len(recipe) == 0:
        print("recipe name cannot be empty")
    elif len(ingredients) == 0:
        print("need a least one ingredient")
    elif len(meal) == 0:
        print("meal name cannot be empty")
    elif not prep_time.isdigit() or len(prep_time) == 0:
        print(
            "all characters in the sting need to be a digit and need at "
            "least one character"
            )
    elif recipe in cookbook.keys():
        print("recipe already in cookbook")
    else:
        cookbook[recipe] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time
        }
        print(f"Adding {recipe} in cookbook:")
        print_dict_items(cookbook)


def print_all_recipes():
    if len(cookbook) > 0:
        print("Listing cookbook recipe:")
        print_dict_keys(cookbook)
    else:
        print("cookbook is empty")


def print_options(list_options):
    print("List of available option:")
    for option_number, option_text in list_options.items():
        print(f"  {option_number}: {option_text}")
    print()


def program_cookbook():
    list_options = {
        '1': 'Add a recipe',
        '2': 'Delete a recipe',
        '3': 'Print a recipe',
        '4': 'Print the cookbook',
        '5': 'Quit'
        }

    print("Welcome to the Python Cookbook !")
    print_options(list_options)
    user_input = input(
        "Please select an option:\n"
        ">> "
        )
    while user_input != '5':
        while user_input is not None and user_input not in list_options.keys():
            print("\nSorry this option does not exist.")
            print_options(list_options)
            user_input = '5'
        if (user_input == '1'):
            recipe = input("\n>>> Enter a name:\n")
            ingredients = []
            ingredients.append(input("\n>>> Enter ingredients:\n"))
            next_ingredient = input()
            while (next_ingredient != ''):
                ingredients.append(next_ingredient)
                next_ingredient = input()

            meal_type = input("\n>>> Enter a meal type:\n")
            prep_time = input("\n>>> Enter a preparation time:\n")
            add_recipe(recipe, ingredients, meal_type, prep_time)
            print()
        elif (user_input == '2'):
            recipe = input("\nRecipe to delete:\n\n")
            delete_recipe(recipe)
            print()
        elif (user_input == '3'):
            recipe = input("\nPlease enter a recipe name to get its details:\n>> ")
            print_recipe(recipe)
            print()
        elif (user_input == '4'):
            print("\n")
            print_all_recipes()
        user_input = input(
            "\nPlease select an option:\n"
            ">> "
        )
    print("\ncookbook closed. Goodbye !")


if __name__ == "__main__":
    program_cookbook()
