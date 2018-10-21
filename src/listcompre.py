new_list = []
for data in range(1, 11):
    new_list.append(data)

print(new_list)

new_list1 = [data for data in range(1, 11)]
print (new_list1)

new_list2 = [data for data in range(1, 11) if data % 2 == 0]
print(new_list2)
