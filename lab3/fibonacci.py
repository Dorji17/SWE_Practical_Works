import time
import math


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

def    fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return[0] 
    
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence 

print(f"fibonacci sequence up to 10 terms: {fibonacci_iterative()}")   

def find_first_fib_exeeding(value):
    a, b = 0, 1
    index = 1
    while b <= value:
        a,b = b, a + b
        index += 1
    return index, b 

value = 100
index, fib_num = find_first_fib_exeeding(value)
print(f"The first fibonacci number exceeding {vale} is f({index}) = {fib_num}")   
      
def is_fibonacci(num):
    return math.isqrt(5 * num**2 + 4) == 5 * num**2 + 4 or math.isqrt(5 * num**2 - 4)**2 == 5 * num**2 - 4

test_numbers = [5, 8, 10, 13]
for number in test_numbers:
    print(f"{number} is a fibonacci number: {is_fibonacci(number)}")     

def fibonacci_ratios(n):
    fib_squence = fibonacci_iterative(n)
    ratios = []
    for i in range(1, len(fib_squence)):
        ratios.append(fib_squence[i] / fib_squence[i -1])
    return ratios

ratios = fibonacci_ratios(10)
print(f"Ratios between consecutive fibonacci numbers:", ratios)
print(f"Appproaching gold ratios:", ratios[-1])

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result}, Time: {iterative_time:.6f} seconds")


def fibonacci_generator(limit):
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")

    
def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]


for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")


n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")

