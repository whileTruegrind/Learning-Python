# Python credit card validator program:
    ## 1 - Remove any "-" or " "
    ## 2 - Add all digits in the odd places from right to left
    ## 3 - Double every second digit from right to left
        ### 3.1 - If result is a two-digit number, add the two-digit number together to get a single digit
    ## 4 - Sum totals of steps 2 & 3
    ## 5 - If sum is divisible by 10, the credit card # is valid

card_number = input("Enter card number: ")

# Step 1:
card_number = card_number.replace("-","")
card_number = card_number.replace(" ","")
card_number = card_number[::-1]
# Step 2:
step2 = 0
for x in card_number[::2]:
    step2 += int(x)
# Step 3:
step3 = 0
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        step3 += (1 + (x % 10))
    else:
        step3 += x
# Step 4:
step4 = step2 + step3
# Step 5:
if step4 % 10 == 0:
    print("Card Valid!")
else:
    print("Card Invalid!")