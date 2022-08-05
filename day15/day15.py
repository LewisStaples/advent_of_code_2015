# adventOfCode 2015 day 15
# https://adventofcode.com/2015/day/15

from collections import OrderedDict



class IngredientData:
    def __init__(self):
        self._ingredients = {}
    
    def import_ingredient(self, input_line):
        input_list = input_line.split(' ')

        ingredient_name = input_list[0][:-1]
        capacity = int(input_list[2][:-1])
        durability = int(input_list[4][:-1])
        flavor = int(input_list[6][:-1])
        texture = int(input_list[8][:-1])
        calories = int(input_list[10])

        self._ingredients[ingredient_name] = {
            'capacity': capacity,
            'durability': durability,
            'flavor': flavor,
            'texture': texture,
            'calories': calories
        }

        dummy = 123

    def createIngAmts(self):
        ret_val = OrderedDict()
        for ingredient_name in self._ingredients:
            ret_val[ingredient_name] = None
        return ret_val




ingredientData = IngredientData()

# Reading input from the input file
input_filename='input.txt'
print(f'\nUsing input file: {input_filename}\n')
with open(input_filename) as f:
    # Pull in each line from the input file
    for in_string in f:
        in_string = in_string.rstrip()
        print(in_string)
        ingredientData.import_ingredient(in_string)

ingredientAmounts = ingredientData.createIngAmts()
TOTAL_AMOUNT = 100
ingred_amt_loop_upper_value = TOTAL_AMOUNT + 1
max_score = float('-inf')




