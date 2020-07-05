name_list = ['Sudarshan', 'Niku', 'Suraj', 'Swapnil']
def find_john(name_list):
    for i in name_list:
        if i == 'John':
            return i

    return "Not found"

print(find_john(name_list))
