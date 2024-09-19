from collections import defaultdict
import ast


def get_unique_ingredients_names(df):
    """the function returns a set of unique
    ingredients names"""
    if 'ingredients' in df.columns:
        def extract_ingredient_names(ingredient_list):
            """the function extracts the value associated
              with the 'name' key from each dictionary"""
            if isinstance(ingredient_list, list):
                return [ingredient['name'] for ingredient in ingredient_list if 'name' in ingredient]
            return []

        # collecting ingredient names:
        ingredient_names = [name for sublist in df['ingredients'].dropna() for name in
                            extract_ingredient_names(sublist)]

        # finding unique ingredient names:
        unique_ingredient_names = set(ingredient_names)
        return unique_ingredient_names
    else:
        return set()  # empty set


def count_drinks_with_ingredient(df):
    """this function counts how many drinks
    contain each unique ingredient"""
    ingredient_count = defaultdict(int)

    for ingredients in df['ingredients'].dropna():
        if isinstance(ingredients, list):
            unique_ingredients = set(ingredient['name'] for ingredient in ingredients if 'name' in ingredient)
            for ingredient in unique_ingredients:
                ingredient_count[ingredient] += 1

    return ingredient_count


def process_ingredients(ingredients):
    """Function that transforms ingredients
    into a list of ingredient names"""

    if isinstance(ingredients, str):
        try:
            ingredients = ast.literal_eval(ingredients)
        except (ValueError, SyntaxError):
            return []
    # if ingredients is a list of dictionaries,
    # we return the names of the ingredients
    if isinstance(ingredients, list):
        return [ingredient['name'] for ingredient in ingredients if isinstance(ingredient, dict)]
    return []

