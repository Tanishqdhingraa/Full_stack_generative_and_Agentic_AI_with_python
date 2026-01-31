chai_type = "Ginger chai"        # string variable
customer_name = "Priya"          # string variable

print(f"Order for {customer_name} : {chai_type} please !")  
# f-string formatting (inject variables into text)

chai_description = "Aromatic and Bold"

print(f"First word: {chai_description[:8]}")   
# string slicing → characters index 0 to 7

print(f"Last word: {chai_description[12:]}")   
# slice from index 12 to end

# chai_description[::-1]  # would reverse the string

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")  
# convert string → bytes

print(f"Non Encoded label: {label_text}")

print(f"Encoded label: {ecoded_label}")      
# shows byte representation

decoded_label = ecoded_label.decode("utf-8")  
# convert bytes → string

print(f"Decoded label: {decoded_label}")
