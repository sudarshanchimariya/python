tuple2 = ([1, 2, 3], 'w', 7, 8, ['wash', 'hand', 'often'], 23, 61)
print('Tuple before removing items: ', tuple2)
#  Since, tuples are immutable we can not remove items.
#  SO, we use + operator for merge of tuples in order to remove items as it will create new tuple.

tuple2 = tuple2[:3] + tuple2[-2:]
print('New tuple: ', tuple2)

                 #OR
# let's convert tuple to list.
list2 = list(tuple2)
print('After converting tuple to list, list: ', list2)
list2.remove("w")
# Now let's convert list to the tuple.
tuple2 = tuple(list2)
print("Tuple after converting list into tuple and removing items: ", tuple2)
