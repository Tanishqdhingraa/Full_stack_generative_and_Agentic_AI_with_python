# CONCEPT: For Loop + Enumerate
# DESCRIPTION: Iterates over a list and gets both index and value

menu = ["Green", "Lemon", "Spiced", "Mint"]  # list of items

for idx, item in enumerate(menu, start=1):   # loop with index starting from 1
    print(f"{idx} : {item} chai")            # display index and item
