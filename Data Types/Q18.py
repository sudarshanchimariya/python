list1 = []
num = int(input("Enter number of items in the list: "))

for i in range(1, num + 1):
    x = int(input("Enter items(number): "))  # x refers items or elements in the list.
    list1.append(x)

print("Largest number from the list is ", max(list1))

