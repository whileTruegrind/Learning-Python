# indexing:
    ## Accessing elements of a sequence using [] (indexing operator)
    ## [start : stop : step]

credit_number = "1234-5678-9012-3456"
                #0123456...........18 
print(credit_number[3])    # 4
print(credit_number[:4])   # 1234
print(credit_number[5:9])  # 5678
print(credit_number[5:])   # 5678-9012-3456
print(credit_number[-1])   # 6

print(credit_number[::2])  # Every 2nd character
print(credit_number[::-1]) # Reverses string