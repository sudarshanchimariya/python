def char_frequency(str):
    obj = {}
    for n in str:
        keys = obj.keys()
        if n in keys:
            obj[n] += 1
        else:
            obj[n] = 1
    return obj
print(char_frequency('google.com'))