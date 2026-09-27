num = input("Enter a number: ").strip()

sum = 0
while True:
    for i in num:
        num_int = int(i)
        sum += num_int
    print(sum)
    break
