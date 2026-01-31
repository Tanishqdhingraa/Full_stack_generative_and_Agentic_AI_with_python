# CONCEPT: Python Dictionaries (Key–Value Data Structure)
# DESCRIPTION: Demonstrates storing, accessing, updating, and removing structured 
# data using dictionary methods

chai_order = dict(type="Masala Chai", size="Large", sugar=2)   # dictionary creation using dict()
print(f"Chai order: {chai_order}")

chai_recipe = {}                                # empty dictionary
chai_recipe["base"] = "black tea"               # add key-value pair
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")    # access value using key
print(f"Recipe: {chai_recipe}")

del chai_recipe["liquid"]                       # delete key-value pair
print(f"Recipe: {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")  # membership test (checks key)

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}  # dictionary literal

# chai_order.keys()    → all keys
# chai_order.values()  → all values
# chai_order.items()   → key-value pairs

last_item = chai_order.popitem()                # removes last inserted key-value pair
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)                # merge another dictionary
print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_order.get("size", "NO Note")  # safe access with default value
print(f"customer_note is: {customer_note}")
