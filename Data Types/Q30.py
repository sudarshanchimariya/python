d1 = {0: 1, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 15, 7: 20}
def check_key_presence(d1, k):
    if k in d1:
        print('Key is present.')
    else:
        print('key is not present.')


check_key_presence(d1, 2)
check_key_presence(d1, 3)
check_key_presence(d1, 5)
check_key_presence(d1, 11)
check_key_presence(d1, 6)
check_key_presence(d1, 10)