def rem_odd_values(str3):
    r = ""     # r for result
    for i in range(len(str3)):
        if i % 2 == 0:
            r = r + str3[i]
    return r

print(rem_odd_values('coursework'))
print(rem_odd_values('123456'))
print(rem_odd_values('pqrstuv'))