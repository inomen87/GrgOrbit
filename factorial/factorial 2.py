def factorial(n):
    if n <= 1:
        return 1
    for num in range(1, n):
        b = n * num
        n = b
    return b


print(factorial(-10))