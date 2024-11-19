my_list=[]

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert

my_list.insert(1,15)

my_list.extend([50,60,70])

print(my_list)
my_list.pop()

print(my_list)

my_list.sort()

#find 30
index_of_30=my_list.index(30)


print("The list after all operations:", my_list)
print("The index of 30 in the list:", index_of_30)