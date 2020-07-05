from math import floor

def binary_search(Array, item):
    n = len(Array)
    L = 0
    R = n-1

    while L <= R:
        mid = floor((L+R)/2)
        if Array[mid] < item:
            L = mid + 1
        elif Array[mid] > item:
            R = mid - 1
        else:
            return "The index of the item : %d" % mid
    return "Item not found: %d" % -1

A = [1, 3, 5, 7, 8, 11, 13, 15, 16, 27, 99]

a = int(input("Enter the number, a value:"))
b = int(input("Enter the number, b value:"))

print(binary_search(A, a))
print(binary_search(A, b))
