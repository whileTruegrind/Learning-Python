# for loops:
    ## Execute a block of code a fixed number of times.
    ## You can iterate over a range, string, sequence etc.

for x in range(1, 11):
    print(x)
print("\n")

for x in reversed(range(1, 11)):
    print(x)
print("Happy New Year!\n")

for x in range(1, 11, 3):
    print(x)
print("\n")

for x in range(1,21):
    if x == 13:
        continue
    print(x)
print("\n")

for x in range(1,21):
    if x == 13:
        break
    print(x)
print("\n")