objects = input("Enter some comma separated sequence of words: ")
words = [w for w in objects.split(",")]   # w for word.
print (",".join(sorted(list(set(words)))))