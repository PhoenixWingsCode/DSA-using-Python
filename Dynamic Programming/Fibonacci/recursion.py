def fib(n):
    if n==1 or n==2:
        result = 1
    else:
        result = fib(n - 1) + fib(n - 2)
    return result

print(f"Fibonacci of 1 is: {fib(1)}")   # Output: 1
print(f"Fibonacci of 2 is: {fib(2)}")   # Output: 1
print(f"Fibonacci of 3 is: {fib(3)}")   # Output: 2
print(f"Fibonacci of 4 is: {fib(4)}")   # Output: 3
print(f"Fibonacci of 5 is: {fib(5)}")   # Output: 5
print(f"Fibonacci of 6 is: {fib(6)}")   # Output: 8
print(f"Fibonacci of 7 is: {fib(7)}")   # Output: 13