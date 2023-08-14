# Python shopping cart program

foods = []
prices = []
total = 0

foodNumber = 1
while True:
    food = input(f"Enter FOOD{foodNumber} to buy (or) \"Q\" to QUIT: ")
    if food.upper() == "Q":
        print("\n~~~~~~ YOUR CART ~~~~~~")
        itemNumber = 0
        for food in foods:
            itemNumber += 1
            print(f"Item{itemNumber}: {food}")
        checkout = input(f"Checkout {itemNumber} items? (Yes/No): ")
        if checkout.lower() == "yes":
            for price in prices:
                total += price
            print(f"\nTOTAL = {total}$")
            break
        else:
            print()
            continue
    else:
        foodNumber += 1
        price = float(input(f"Enter the price of {food}: $"))
        foods.append(food)
        prices.append(price)