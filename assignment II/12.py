# Create a function, is_palindrome, to determine if a supplied word is
# the same if the letters are reversed.

def is_palindrome(s):
    s = s.lower()
    if s == s[::-1]:
        print(s, "is a palindrome.")
    else:
        print(s, "is not a palindrome.")


word = input("Enter a word to check palindrome: ")
is_palindrome(word)
