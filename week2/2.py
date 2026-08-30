list_numbers = list(range(1, 10))

count = list_numbers[0]

for i in list_numbers:
    if i > count:
        count = i

print(count)
