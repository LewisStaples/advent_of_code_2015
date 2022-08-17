# adventOfCode 2015 day 20
# https://adventofcode.com/2015/day/20

# This program uses sympy.ntheory.factorint to factor integers to all prime number factors
# See below link for details
# https://docs.sympy.org/latest/modules/ntheory.html?highlight=factorint#sympy.ntheory.factor_.factorint
import sympy.ntheory

house_number = 2
while True:
# for some_random_indexer in range(200):
    # Use logic to calculate which elves visit from part A
    elves_visiting = {1}
    # Loop thru dict of prime numbers of number of times that prime is in the house_number
    # (This dict was created by factoring house_number into its prime numbers)
    for k,v in sympy.ntheory.factorint(house_number).items():
        # Construct a new set by multiplying all multiples of this prime number against set elves_visiting
        new_subset = set()
        for i in range(v):
            new_subset.update({el*k**(i+1) for el in elves_visiting})
        elves_visiting.update(new_subset)
    
    # Use new logic for part B to account for elves only visiting 50 houses
    if house_number / 50 == house_number // 50:
        elf_cut_off = (house_number - 1) // 50
    else:
        elf_cut_off = house_number // 50

    # Then all elfs numbered elf_cut_off and below should be removed from set elves_visiting
    # (this is more part B logic)
    elves_visiting = {x for x in elves_visiting if x > elf_cut_off}

    # Calculate the number of presents delivered (and compare to target value)
    # (Logic is unchanged for part B, but one constant below is now 11, instead of 10)
    if 11 * sum(elves_visiting) > 29000000:
        break
    house_number += 1

print(f'\nThe house number (the answer to part B) is {house_number}\n')


