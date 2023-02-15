import time
import matplotlib.pyplot as plt

# Recursive Fibonacci function without memoization
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
# Memoized Fibonacci function with memoization
def fib_memoized(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    result = fib_memoized(n-1, memo) + fib_memoized(n-2, memo)
    memo[n] = result
    return result
# List to store execution times for the recursive and memoized functions
recursive_timings = []
memorized_timings = []

# Loop over values of n from 0 to 35
for n in range(36):
    # Time the execution of the recursive function for the current value of n
    start = time.time()
    result = fib_recursive(n)
    end = time.time()
    recursive_timings.append(end - start)

    # Time the execution of the memoized function for the current value of n
    start = time.time()
    result = fib_memoized(n)
    end= time.time()
    memorized_timings.append(end - start)

# Plot the execution times for the recursive and memoized functions
plt.plot(range(36), recursive_timings, label='Recursive')
plt.plot(range(36), memorized_timings, label='Memorized')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.show()