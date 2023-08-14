# Collection
    ## Single variable used to store multiple values
    ## List []
        ### Ordered and changeable. Duplicates OK
    ## Set {}
        ### Unordered and immutable, but add/remove OK. NO duplicates
    ## Tuple ()
        ### Ordered and unchangeable. Duplicates OK. Faster.

print("\n\n~~~~~~~~~~~~~~~~~~~~~~LISTS~~~~~~~~~~~~~~~~~~~~~~")
# LISTS
fruits = ["apple", "orange", "pear", "banana", "mango"]

print(fruits[:])

fruits.append("pineapple")
for fruit in fruits:
    print(fruit, end = " ")
print()

fruits.remove("apple")
for fruit in fruits:
    print(fruit, end = " ")
print()

fruits.insert(1, "apple")
for fruit in fruits:
    print(fruit, end = " ")
print()

fruits.sort()
for fruit in fruits:
    print(fruit, end = " ")
print()

fruits.reverse()
for fruit in fruits:
    print(fruit, end = " ")
print()

print(fruits.index("apple"))

fruits.clear()
for fruit in fruits:
    print(fruit, end = " ")
    
print("\n\n~~~~~~~~~~~~~~~~~~~~~~SETS~~~~~~~~~~~~~~~~~~~~~~")
# SETS
fruits = {"apple", "orange", "pear", "banana", "mango"}

print(len(fruits))
print(fruits)

print("pineapple" in fruits)

fruits.add("pineapple")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

print("\n\n~~~~~~~~~~~~~~~~~~~~~~TUPLES~~~~~~~~~~~~~~~~~~~~~~")
# TUPLES
fruits = ("apple", "orange", "pear", "banana", "mango")

print(fruits)

print(fruits.index("apple"))

print(fruits.count("apple"))