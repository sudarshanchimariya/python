def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                return False
                break
        else:
            return True
number = int(input("Enter a number:"))
print(is_prime(number))
