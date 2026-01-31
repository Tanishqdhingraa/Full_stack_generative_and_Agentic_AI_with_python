# CONCEPT: Python Lists & Bytearray
# DESCRIPTION: Demonstrates mutable sequences, list operations, and basic byte-level 
# data manipulation

ingredients = ["water", "milk", "black tea"]      # list (mutable collection)
ingredients.append("sugar")                       # add item at end
print(f"Ingredients are: {ingredients}")

ingredients.remove("water")                      # remove specific item
print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)            # merge another list
print(f"chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")           # insert at specific index
print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()               # remove & return last item
print(f"{last_added}")
print(f"chai: {chai_ingredients}")

chai_ingredients.reverse()                        # reverse list order
print(f"chai: {chai_ingredients}")

chai_ingredients.sort()                           # sort list alphabetically
print(f"chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}") # largest value
print(f"Minimum sugar level: {min(sugar_levels)}") # smallest value

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor      # list concatenation
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3          # repeat list elements
print(f"String brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")           # mutable byte sequence
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")  # byte replacement
print(f"Bytes: {raw_spice_data}")
