list2 = [{}, {}, {}]
list3 = [{1, 2}, {}, {}]
print(all(not dict for dict in list2))
print(all(not dict for dict in list3))
