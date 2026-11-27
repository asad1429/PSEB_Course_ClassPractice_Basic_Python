age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print(f"Not eligible. You need to wait {18-age} years more.")