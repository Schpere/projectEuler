def is_palindrome(n):
    return str(n) == str(n)[::-1]

largest = 0

for n in range(100,1000):
    for m in range(100,1000):
        number = n * m
        if is_palindrome(number) and number > largest:
            largest = number
print largest
