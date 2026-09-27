

### 1. Create Strings in Different Ways

# Different ways to create strings
s1 = "Hello"        # double quotes
s2 = 'World'        # single quotes
s3 = str("Python")  # str() constructor
s4 = str()          # empty string

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))


### 2. Immutable Strings Demo

s = "hello"
print("Original string:", s)
print("Memory address:", id(s))

# Modify string (creates new object)
s = s + " world"
print("Modified string:", s)
print("New memory address:", id(s))


### 3. Concatenation and Repetition


s1 = "Python"
s2 = "Rocks"

# Concatenation
print(s1 + " " + s2)

# Repetition
print(s1 * 3)


### 4. String Slicing Practice


s = "welcome"

print("Characters from index 1 to 4:", s[1:5])   # "elco"
print("First 5 characters:", s[:5])              # "welco"
print("Last 3 characters:", s[-3:])              # "ome"
print("Middle substring 'lco':", s[2:5])         # "lco"


### 5. Check Substring using `in` and `not in`

word = input("Enter a word: ")

if "python" in word:
    print("Found")
else:
    print("Not Found")


### 6. String Formatting with f-strings


name = input("Enter your name: ")
age = input("Enter your age: ")

print(f"My name is {name}, and I am {age} years old.")


### 7. Case Conversion Methods


s = "welcome to python"

print("capitalize():", s.capitalize())  # "Welcome to python"
print("title():", s.title())            # "Welcome To Python"
print("upper():", s.upper())            # "WELCOME TO PYTHON"
print("swapcase():", s.swapcase())      # "WELCOME TO PYTHON"


### 8. Counting and Replacing


s = "banana"
print("Count of 'a':", s.count("a"))

sentence = "I like banana"
new_sentence = sentence.replace("banana", "orange")
print(new_sentence)


### 9. Validation Check


text = input("Enter a string: ")

print("Is alphabet only? ", text.isalpha())
print("Is digits only? ", text.isdigit())
print("Is alphanumeric? ", text.isalnum())


### 10. Split and Strip


s = "  apple,banana,grape  "

# Strip spaces
s = s.strip()

# Split by comma
fruits = s.split(",")

print("Fruits:", fruits)