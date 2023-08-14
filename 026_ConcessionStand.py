# Python Concession Stand program

menu = {"Popcorn": 100,
         "Nachos": 80,
          "Fries": 40,
          "Pizza": 200,
          "Combo": 400}
cart = []
total = 0

print("~~~~~~~~~~ MENU ~~~~~~~~~~")
for key,value in menu.items():
    print(f"{key:<7} ---------- {value:6.2f}$")
print()

item_number = 1
while True:
    item = input(f"Enter \"Done\" when DONE (or) Enter Item {item_number}: ").capitalize()
    if item == "Done":
        print("~~~~~~~~~~ CART ~~~~~~~~~~")
        for item in cart:
            print(f"{item:<7} ---------- {menu.get(item):6.2f}$")
        print(f"TOTAL   ********** {total:6.2f}$")
        break
    elif item not in menu:
        print(f"{item} doesn't exist!")
    else:
        cart.append(item)
        total += menu.get(item)
        item_number += 1