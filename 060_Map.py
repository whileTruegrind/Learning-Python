store = [
   ("Shirt", 550),
   ("Pant", 1200),
   ("Sweatshirt", 700),
   ("Socks", 50)
]

to_dollars = lambda store : (store[0], round(store[1] / 82.653, 2))
store_dollars = list(map(to_dollars, store))

for item in store_dollars:
    print(item)