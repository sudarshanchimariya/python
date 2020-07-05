tup_list = [('Sudarshan', 'Chimariya', 23), ('Niku', 'Thapa', None),
            ('Nishan', 'Magar', 16), ('Nischal', 'Pathak', 25), ('Prakrity', 'Thapa', 23)]

age = []
full_name = ''

for i in range(len(tup_list)):
    if tup_list[i][2]:
        age.append(tup_list[i][2])

avg_age = sum(age) / len(age)

for i in range(len(tup_list)):
    full_name = tup_list[i][0] + ' ' + tup_list[i][1]
    if tup_list[i][2]:
        if tup_list[i][2] < avg_age:
            print(full_name + ' is young')
        else:
            print(full_name + ' is old')
    else:
        print("#", full_name)
