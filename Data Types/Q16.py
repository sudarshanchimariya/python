#l = [2, 3, 4, 5, -6]  # l is list.
#total = sum(l)
#print("Sum of items in the list:", total)

list1 = []
num = int(input("Enter number of items in the list: "))

for i in range(0, num + 1):
    x = int(input("Enter items(number): "))  # x refers items or elements in the list.
    list1.append(x)

print("Sum of items in the list: ", sum(list1))