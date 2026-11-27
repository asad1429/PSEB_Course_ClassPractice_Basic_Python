#Print the first city, the last city, the middle three cities (using slicing) and the whole list reversed
cities = ["Lahore", "Karachi", "Multan", "Quetta", "Peshawar"]
print(cities[0])
print(cities[-1])
print(cities[1:4])
print(cities[::-1])


#Exercise 2: Marks report 
marks = [78, 92, 65, 88, 54]
print(sum(marks))
print(avg := sum(marks) / len(marks))
print(max(marks))
print(min(marks))


#Exercise 3: Shopping list 
shopping_list = ["bread", "milk", "eggs"]
print(shopping_list)
shopping_list.append("rice")
print(shopping_list)
shopping_list.insert(1, "sugar")
print(shopping_list)
shopping_list.remove("milk")
print(shopping_list)
shopping_list.pop()
print(shopping_list)

#Level 2: Think a little 
#Exercise 4: Remove duplicates 
num =  [3, 1, 3, 2, 1, 5]
unique_num = []
for n in num:
    if n not in unique_num:
        unique_num.append(n)
print(unique_num)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for n in numbers:
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

