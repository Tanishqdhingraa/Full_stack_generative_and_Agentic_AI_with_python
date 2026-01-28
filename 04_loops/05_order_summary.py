names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]


# name goes for names 
# bills goes for amount 
for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")