def add(x):
    length = len(x)
    if length >= 3:
        if x[-3:] == 'ing':
            x += 'ly'
        else:
            x += 'ing'
    return x

print(add('abc'))
print(add('string'))
print(add('ab'))