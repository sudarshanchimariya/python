import csv

with open('file.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    list_of_dict = []
    for row in reader:
        list_of_dict.append(dict(row))
    print(list_of_dict)
