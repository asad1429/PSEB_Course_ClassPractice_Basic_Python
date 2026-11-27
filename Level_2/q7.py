bill_amount = int(input("Enter the bill amount: "))

if bill_amount >= 5000:
    discount = bill_amount * 0.10
    final_amount = bill_amount - discount
    print(f"You got a discount of {final_amount}.")
elif bill_amount >= 2000 and bill_amount <= 4999:
    discount = bill_amount * 0.05
    final_amount = bill_amount - discount
    print(f"You got a discount of {final_amount}.")
else:
    print("No discount available.")
   