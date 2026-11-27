'''''
nums = { "values": [3, 5, 3, 8, 5, 3, 9] 
}

for i in nums["values"]:

    i = set(nums["values"])
    total_unique = len(set(nums["values"]))
print(f"Unique values: {i}")
print(f"Total unique values: {total_unique}")
'''
nums = [3, 5, 3, 8, 5, 3, 9]
unique_values = []
for i in nums:
    if i not in unique_values:
        unique_values.append(i)

print(f"Unique values: {unique_values}")
print(f"Total unique values: {len(unique_values)}")