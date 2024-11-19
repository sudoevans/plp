numbers=input("Enter numbers to add separated by commas")

int_list=[int(i) for i in numbers.split(',')]

total=sum(int_list)
print(total)

