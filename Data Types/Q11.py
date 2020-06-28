def count_word (str4):
    counts = dict()
    words = str4.split()
    for w in words:  # w for word.
        if w in counts:
            counts[w] += 1
        else:
            counts[w] = 1

    return counts

print(count_word("Hi! Welcome to my world of coding."))
