def longest_one (w_list):
    w_length = []
    for x in w_list:
        w_length.append((len(x), x))
    w_length.sort()
    return w_length[-1][1]

print(longest_one(["War", "Python","Snake","Assignment"]))

