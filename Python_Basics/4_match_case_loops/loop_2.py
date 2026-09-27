word = input("Enter a word: ").lower().strip()

if word in ("a", "e", "i", "o", "u"):
    print("Vowels")
else:
    print("Consonant")