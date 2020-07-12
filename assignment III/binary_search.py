def binary_search(item_list, item):
    first = 0
    last = len(item_list) - 1
    found = False
    while (first <= last and not found):
        mid = (first + last) // 2
        if item_list[mid] == item:
            found = True
        else:
            if item < item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

item_list = [1, 2, 3, 5, 8]
item = int(input("Enter a number to check the existence of element-number in array: "))

output = binary_search(item_list, item)

if output == True:
    print("The element exists"+ str(binary_search(item_list,item)))
else:
    print("Element does not exist")