def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    
    if n == 1 or n == 2:
        return 1
    
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]

n = 10
memo = [None] * (n + 1)  # memo[0] to memo[n]

print(f"Fibonacci of {n} is:", fib(n, memo))