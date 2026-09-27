mark = float(input("Enter your marks "))

if mark > 90:
    print("A")
elif 90 > mark > 80:
    print("B")
elif 80 > mark > 55:
    print("C")
elif 55 > mark > 40:
    print("D")
else:
    print("F")