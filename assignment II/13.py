info = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

def write_csv(data):
    file = open("file.csv", "w+")
    file.write('name,address,age \n')
    for i in range(len(data)):
        value = tuple(map(str, data[i]))
        single = ','.join(value)
        file.write(single + '\n')

    file.close()

write_csv(info)
