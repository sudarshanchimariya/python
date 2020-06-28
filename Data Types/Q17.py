def multiple_items(a):
    m_num = 1   # m_num refers result of multiplications of numbers in the list.
    for n in a:   # a refers items.
        m_num = m_num * n
    return m_num

print(multiple_items([2, 3, 8, -9]))
print(multiple_items([3, 9, -3, 0]))
print(multiple_items([4, 2, 7, -1, -3, 2]))

