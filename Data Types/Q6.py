def appear_not_poor (a):
    str_not = a.find('not')
    str_poor = a.find('poor')

    if str_poor>str_not and str_not>0 and str_poor>0:
        new_a = a.replace(a[str_not:(str_poor+4)], 'good')
        return new_a
    else:
        return a


print(appear_not_poor('The lyrics is not that poor!'))
print(appear_not_poor('The lyrics is poor!'))