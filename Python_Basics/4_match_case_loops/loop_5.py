num = input("Enter a number: ")

# Handle negative numbers
if num.startswith("-"):
    reversed_num = "-" + num[:0:-1]
else:
    reversed_num = num[::-1]

print("Reversed:", int(reversed_num))