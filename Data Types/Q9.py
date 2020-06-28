def exchange_char (str2):
    return str2[-1:] + str2[1:-1] + str2[:1]

print(exchange_char('king'))
print(exchange_char('Red'))
print(exchange_char('study'))