def interpolation_search(arr_list, low, high, a):

    if (low <= high and a >= arr_list[low] and a <= arr_list[high]):
        position = low + ((high - low) // (arr_list[high] - arr_list[low]) * (a - arr_list[low]))
        if arr_list[position] == a:
            return position

        if arr_list[position] < a:
            return interpolation_search(arr_list, position + 1, high, a)

        if arr_list[position] > a:
            return interpolation_search(arr_list, low, position - 1, a)
    return -1


arr_list = [15,36,44,25,56,63,69,42,90]
a = int(input("Enter a number: "))
index = interpolation_search(arr_list, 0, len(arr_list) - 1, a)

if index != -1:
    print("The element exists", index)
else:
    print("The element does not exist.")