def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1

if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib, end=' ')
    print()
    print(sum(fibonacci(100)))