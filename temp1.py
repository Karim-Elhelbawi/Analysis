
#Question 1 part a,i
def iterative(x, y):
    res = 1
    i = 1
    while i <= y:
        res *= x
        i += 1
    return res


#Question 1 part a,ii
def conquer(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half_pow = conquer(a, n // 2)
        return half_pow * half_pow
    else:
        half_pow = conquer(a, (n - 1) // 2)
        return half_pow * half_pow * a


#Question 1 part c
import time
import matplotlib.pyplot as plt

def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return result, elapsed_time

n_values = list(range(1, 100001, 10000))  # Values of n from 1 to 100,000
naive_times = []
divide_conquer_times = []

for n in n_values:
    _, naive_time = measure_time(iterative, 2, n)
    _, divide_conquer_time = measure_time(conquer, 2, n)
    naive_times.append(naive_time)
    divide_conquer_times.append(divide_conquer_time)

# Plot the experimental results
plt.figure(figsize=(10, 6))
plt.plot(n_values, naive_times, label='Naive Iterative Method')
plt.plot(n_values, divide_conquer_times, label='Divide-and-Conquer Method')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.legend()
plt.title('Algorithm Scalability')
plt.grid(True)
plt.show()
