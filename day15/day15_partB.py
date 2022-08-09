# adventOfCode 2015 day 15
# https://adventofcode.com/2015/day/15

import itertools

class IngredientData:
    def __init__(self):
        self._ingredients = {}
        self._property_name_list = [
            'capacity',
            'durability',
            'flavor',
            'texture',
            'calories'
        ]
    
    def import_ingredient(self, input_line):
        input_list = input_line.split(' ')

        ingredient_name = input_list[0][:-1]
        capacity = int(input_list[2][:-1])
        durability = int(input_list[4][:-1])
        flavor = int(input_list[6][:-1])
        texture = int(input_list[8][:-1])
        calories = int(input_list[10])

        # Index is ingred. name, 
        # value is ingred. properties per unit
        self._ingredients[ingredient_name] = {
            'capacity': capacity,
            'durability': durability,
            'flavor': flavor,
            'texture': texture,
            'calories': calories
        }

    def get_score(self, permutation):
        ret_val = 1
        for property in self._property_name_list[:-1]:
            property_val = 0
            for i, ingredient in enumerate(self._ingredients):
                property_val += permutation[i] * self._ingredients[ingredient][property]
            if property_val < 0:
                property_val = 0
            ret_val *= property_val
        
        calorie_count = 0
        for i, ingredient in enumerate(self._ingredients):
            calorie_count += permutation[i] * self._ingredients[ingredient]['calories']
        if calorie_count != 500:
            # Eliminate this from being considered as the maximum (because it isn't 500 calories)
            ret_val = float('-inf')
        return ret_val

ingredientData = IngredientData()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        ingredientData.import_ingredient(in_string)

max_score = float('-inf')
all_permutations = itertools.product(range(101), repeat=len(ingredientData._ingredients))
for permutation in all_permutations:
    if sum(permutation) == 100:
        max_score = max(max_score, ingredientData.get_score(permutation))

print(f'\nThe answer to part A is {max_score}\n')
