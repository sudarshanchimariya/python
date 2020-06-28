def add_tags(t, w):
    return "<%s>%s<%s>" % (t, w, t)    # t for tag and w for word.
print(add_tags('i', 'Python'))
print(add_tags('b', 'Python Tutorial'))
print(add_tags('p', "Let's complete the task."))