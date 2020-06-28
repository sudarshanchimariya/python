def single_str(str1, str2):
    p = str2[:2] + str1[2:]
    q = str1[:2] + str2[2:]
    return p + ' ' + q

print(single_str('abc', 'xyz'))