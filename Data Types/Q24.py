def clone_list(l1):
    c_list = l1[:]  # c_list refers clone list of original list.
    return c_list

l1 = [1, 2, 3, 4, 5, 6]
c_list = clone_list(l1)
print("Actual list is ", l1)
print("Clone list is ", c_list)