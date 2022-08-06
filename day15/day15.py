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

        # Index is ingred. name, 
        # value is ingred. characteristics per unit
        self._ingredients[ingredient_name] = {
            'capacity': capacity,
            'durability': durability,
            'flavor': flavor,
            'texture': texture,
            'calories': calories
        }

    def get_total_score(self, ingredientAmounts):
        ret_val = 43

        dummy = 123


        return ret_val



    def createIngAmts(self):
        ret_val = OrderedDict()
        for ingredient_name in self._ingredients:
            ret_val[ingredient_name] = None
        return ret_val


    def choose_next_ingred_amount(self, ingredientAmounts, ingred_amt_loop_upper_value, ingredientData):
        i_ing_next = list(ingredientAmounts.values()).index(None)
        if i_ing_next == len(ingredientAmounts) - 1:
            # NEED TO FIX ...
            # ingredientAmounts[-1] = ingred_amt_loop_upper_value - 1
            return self.get_total_score(ingredientAmounts)

        ret_val = float('-inf')
        for ingred_amount in range(0, ingred_amt_loop_upper_value):
            # NEED TO FIX ....
            # ingredientAmounts[self._ingredients[i_ing_next]] = ingred_amount
            ingred_amt_loop_upper_value -= ingred_amount
            # FIXING ABOVE SHOULD FIX THIS .....
            # ret_val = max(ret_val, self.choose_next_ingred_amount(ingredientAmounts, ingred_amt_loop_upper_value, ingredientData))
        return ret_val


ingredientData = IngredientData()

# Reading input from the input file
input_filename='input_sample0.txt'
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

# next try recursion to choose ingredient amounts 
ingredientData.choose_next_ingred_amount(ingredientAmounts, ingred_amt_loop_upper_value, ingredientData)

dummy = 123

