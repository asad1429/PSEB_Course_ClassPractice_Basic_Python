Char = input("Enter your character: ")
if Char in "AEIOUaeiou":
    print("The character is a vowel.")
elif Char in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz":
    print("The character is a consonant.")
elif Char.isdigit():
    print("The character is a digit.")
elif Char.isalpha():
    print("The character is a special character.")
else:
    print("Invalid input.")
