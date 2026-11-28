list = int(input("Enter the number of elements in the list: "))
elements = []
for i in range(list):
    element = int(input(f"Enter element {i + 1}: "))
    elements.append(element)
print(f"The list of elements is: {elements}")