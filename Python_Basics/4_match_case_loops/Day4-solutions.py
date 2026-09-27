
## 1. Positive, Negative, or Zero

num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


## 2. Vowel or Consonant

ch = input("Enter a single letter: ").lower()

if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant")


## 3. Grading System

score = int(input("Enter score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)



## 4. Sum of Digits


num = int(input("Enter a number: "))
total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of digits:", total)



## 5. Reverse a Number


num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)


## 6. Multiplication Table

n = int(input("Enter a number: "))

for i in range(1, 11):
    print("{0} x {1} = {2}".format(n,i,n*i))


## 7. Print a Square


size = int(input("Enter size of square: "))

for i in range(size):
    print("* " * size)


## 8. Sum of First 'n' Numbers


n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum of first", n, "numbers is", total)


## 9. Count Vowels in a Word


word = input("Enter a word: ").lower()
count = 0

for ch in word:
    if ch in 'aeiou':
        count += 1

print("Number of vowels:", count)


## 10. Fibonacci Sequence


n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b


## 11. Input Validation with break


while True:
    num = int(input("Enter a number between 1 and 10: "))
    if 1 <= num <= 10:
        print("Valid number entered:", num)
        break
    else:
        print("Invalid! Try again.")


## 12. Skip Multiples with continue


for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)


## 13. Simple ATM Simulator

balance = 0

while True:
    print("\nATM Menu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Balance:", balance)
    elif choice == "2":
        amount = float(input("Enter withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Balance:", balance)
        else:
            print("Insufficient balance!")
    elif choice == "3":
        print("Exiting ATM. Goodbye!")
        break
    else:
        print("Invalid choice!")


## 14. Count 'a's and 'b's


word = input("Enter a word: ").lower()
count_a = 0
count_b = 0

for ch in word:
    if ch == 'a':
        count_a += 1
    elif ch == 'b':
        count_b += 1
    else:
        continue

print("'a' count:", count_a)
print("'b' count:", count_b)
