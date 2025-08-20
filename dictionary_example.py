#for temporary/counter in range(): 
# for any in range(5): #range generates numbers 0 through 4
#     print("Hello!")


# # Define a list of pet names.
pets = ["Buddy", "Mittens", "Goldie", "Spike", "Bella"] 

# for each_pet in pets:
#     print(each_pet)

# # Loop forward through the list using range() 
for i in range(len(pets)): #start at 0, end before 5
    # Start at 0, stop at the length of the list, step by 1. 
    print(f"Pet {i}: {pets[i]}")