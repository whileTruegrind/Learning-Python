# 2D Collections
    ## A Two Dimensional collection is defined as an Collection inside the Collection

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for foods in groceries:
    for food in foods:
        print(food, end = " ")
    print()

# KEYPAD exercise
print("\n\n~~~~~~~~~~~~~~ KEYPAD ~~~~~~~~~~~~~~\n")

num_pad = ((1,2,3),(4,5,6),(7,8,9),("#",0,"*"))

for row in num_pad:
    for column in row:
        print(column, end = "    ")
    print("\n")