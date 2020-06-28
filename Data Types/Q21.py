def last_k(x):
    return x[-1]

def sort_out_list_last(t):  # t for tuples.
    return sorted(t, key=last_k)

print(sort_out_list_last([(2,5), (1,2), (4,4), (2,3), (2,1)]))
print(sort_out_list_last([(2,3), (3,6), (5,7), (1,9), (2, 0)]))
