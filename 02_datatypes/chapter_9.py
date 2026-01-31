# CONCEPT: Python Sets & Set Operations
# DESCRIPTION: Demonstrates unique collections and mathematical set logic 
# like union, intersection, and difference

essential_spices = {"cardamom", "ginger", "cinnamon"}   # set (unique items)
optional_spices = {"cloves", "ginger", "black pepper"}  # another set

all_spices = essential_spices | optional_spices         # union (combine unique items)
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices      # intersection (common items)
print(f"common spices: {common_spices}")

only_in_essential = essential_spices - optional_spices  # difference (items only in first set)
print(f"Only in essential spices: {only_in_essential}")

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}")  # membership test
