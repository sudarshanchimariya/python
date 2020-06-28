def str_me(input_str):
    if len(input_str) < 2:
        return 'empty'

    return input_str[0:2] + input_str[-2:]


if __name__ == "__main__":
    string_made = input('Enter the string: ')
    print(str_me(string_made))
