def get_str(str1):
    character = str1[0]
    str1 = str1.replace(character, '$')
    str1 = character + str1[1:]

    return str1

if __name__ == "__main__":
    string_made = input('Enter the string: ')
    print(get_str(string_made))