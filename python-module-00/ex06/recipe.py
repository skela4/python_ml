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
    if recipe not in cookbook.keys():
        print("recipe not in cookbook")
    else:
        print(f"Recipe for {recipe}:")
        print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
        print(f"To be eaten for {cookbook[recipe]['meal']}")
        print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking.")


def delete_recipe(recipe):
    if recipe not in cookbook.keys():
        print("recipe not in cookbook")
    else:
        print(f"Deleting {recipe} from cookbook:")
        del cookbook[recipe]
        print_dict_items(cookbook)
#TODO meilleur split des ingredients
def add_recipe(recipe, ingredients, meal, prep_time):
    if recipe in cookbook.keys():
        print("recipe already in cookbook")
    else:
        print(f"Adding {recipe} in cookbook:")
        cookbook[recipe] = {
            'ingredients': ingredients,
            'meal': meal,
            'prep_time': prep_time
        }
        print_dict_items(cookbook)


def print_all_recipes():
    print("Listing cookbook recipe:")
    print_dict_keys(cookbook)

import string
def program_cookbook():
    list_options = {
        '1': 'Add a recipe',
        '2': 'Delete a recipe',
        '3': 'Print a recipe',
        '4': 'Print the cookbook', 
        '5': 'Quit',
        }
    print("Please select an option by typing the corresponding number:")
    for option_number, option_text in list_options.items():
                print(f"{option_number}: {option_text}")
    user_input = input()
    while user_input != None and user_input not in list_options.keys():
        print("This option does not exist, please type the corresponding number.")
        print("To exit, enter 5")
        for option_number, option_text in list_options.items():
            print(f"{option_number}: {option_text}")
        user_input = input()
    
    if (user_input == '1'):
        recipe = input("\nRecipe name:\n")
        ingredients = input("ingredients:\n")
        ingredients = ingredients.split(',')
        meal_type = input("Type of meal:\n")
        prep_time = input("Time of prep:\n")
        add_recipe(recipe, ingredients, meal_type, prep_time)
    elif (user_input == '2'):
        recipe = input("\nRecipe to delete:\n\n")
        delete_recipe(recipe)
    elif (user_input == '3'):
        recipe = input('\nRecipe name:\n\n')
        print_recipe(recipe)
    elif (user_input == '4'):
        print("\n")
        print_all_recipes()
    elif (user_input == '5'):
        print("\ncookbook closed")
        exit(0)


if __name__ == "__main__":
    program_cookbook()