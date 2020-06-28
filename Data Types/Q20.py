def count_num_str(a):
    x = 0
    for w in a:  # a refers words and w refers word among words.
        if len(w) >= 2 and w[0] == w[-1]:
            x = x+1
    return x

print(count_num_str(['abc', 'xyz', 'aba', '1221']))
print(count_num_str(['wow', 'nice', 'songs', '2222']))