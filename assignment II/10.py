def change_to_snake_case(insert_string):
    return ''.join(['_' + i.lower() if i.isupper()
                    else i for i in insert_string]).lstrip('_')


def change_to_kebab_case(insert_string, separator):
    letters = change_to_snake_case(insert_string)
    print("Kebab case strings:", letters.replace('_', separator))

x = "ThisIsCamelCased"
print("Camel case strings:", x)
print("Snake case strings:", change_to_snake_case(x))

change_to_kebab_case(x, '-')