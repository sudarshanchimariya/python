full_name = ('Sudarshan', 'Chimariya', 23)
print("This is tuple:", full_name)
a_list = []
a_list.append(full_name)
full_name1 = ('suraj', 'shrestha', 22)
full_name2 = ('vijay', 'pathak', 22)
a_list.append(full_name1)
a_list.append(full_name2)

sort = sorted(a_list, key=lambda tup: tup[2])


print("List of tuples after sorting out:",(sort))
