def remove_string_character (str1, n):
    a = str1[:n]
    b = str1[n+1:]
    return a + b
print(remove_string_character('Assignment', 1))
print(remove_string_character('Assignment', 4))
print(remove_string_character('Assignment', -3))
print(remove_string_character('Assignment', -8))
print(remove_string_character('Assignment', 5))