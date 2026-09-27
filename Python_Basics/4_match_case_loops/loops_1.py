
while True:
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input! '0.00' is a decimal. Please enter a whole integer.")
    else:
        if num > 0:
            print("Positive")
        elif num == 0:
            print("Zero")
        else:
            print("Negative")
        break