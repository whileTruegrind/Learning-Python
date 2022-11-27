# format specifiers = {:flags} format a value based on what flags are inserted 
    ## .(number)f = round to that many decimal places
    ## :(number) = allocate that many spaces
    ## :0(number) = allocate and zero pad that many spaces
    ## :< = left justify
    ## :> = right justify
    ## :^ = center align
    ## :+ = use a plus sign to indicate positive value
    ## := = place sign to leftmost position
    ## :  = insert a space before positive numbers
    ## :, = comma separator
    ## :% = percentage format

price1 = 3.14959
price2 = -987.333
price3 = 34455412.34354

print(f"Price 1: ${price1:.2f}")
print(f"Price 2: ${price2:.2f}")
print(f"Price 3: ${price3:.2f}\n")

print(f"Price 1: ${price1:010}")
print(f"Price 1: ${price1:<10}")
print(f"Price 1: ${price1:>10}")
print(f"Price 1: ${price1:^10}")

print(f"Price 1: ${price3:+,.2f}")