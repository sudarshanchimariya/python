def insert_string_middle(str5, w):
    return str5[:2] + w + str5[2:]   # w for word.

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
