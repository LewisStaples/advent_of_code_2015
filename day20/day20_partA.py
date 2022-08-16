# adventOfCode 2015 day 20
# https://adventofcode.com/2015/day/20

# This program uses sympy.ntheory.factorint to factor integers to all prime number factors
# See below link for details
# https://docs.sympy.org/latest/modules/ntheory.html?highlight=factorint#sympy.ntheory.factor_.factorint
import sympy.ntheory

house_number = 2
while True:
    elves_visiting = {1}
    # Loop thru dict of prime numbers of number of times that prime is in the house_number
    # (This dict was created by factoring house_number into its prime numbers)
    for k,v in sympy.ntheory.factorint(house_number).items():
        # Construct a new set by multiplying all multiples of this prime number against set elves_visiting
        new_subset = set()
        for i in range(v):
            new_subset.update({el*k**(i+1) for el in elves_visiting})
        elves_visiting.update(new_subset)
    # Calculate the number of presents delivered (and compare to target value)
    if 10 * sum(elves_visiting) > 29000000:
        break
    house_number += 1

print(f'\nThe house number (the answer to part a) is {house_number}\n')


